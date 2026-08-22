import os
import sys
import urllib.request
import django
from PIL import Image, ImageFilter, ImageEnhance

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

try:
    django.setup()
except Exception as e:
    print(f"Setup error: {e}")
    sys.exit(1)

from shop.models import Blog

MEDIA_BLOGS_DIR = os.path.join('media', 'blogs')
os.makedirs(MEDIA_BLOGS_DIR, exist_ok=True)

# Function to render an ultra-crisp 1000x1000 canvas card
def create_1000x1000_card(src_path, dst_path):
    try:
        orig = Image.open(src_path).convert("RGBA")
        
        # 1. Canvas 1000x1000 px
        W, H = 1000, 1000
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        
        o_w, o_h = orig.size
        # Margin of 80px -> inner box 840x840 px
        max_w, max_h = 840, 840
        ratio = min(max_w / o_w, max_h / o_h)
        
        new_w = max(1, int(o_w * ratio))
        new_h = max(1, int(o_h * ratio))
        
        # 2. High-quality LANCZOS resampling
        resized = orig.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Center image on canvas
        pos_x = (W - new_w) // 2
        pos_y = (H - new_h) // 2
        
        canvas.paste(resized, (pos_x, pos_y), resized)
        
        # 3. Convert to RGB
        final_rgb = canvas.convert("RGB")
        
        # 4. Apply UnsharpMask for ultra clarity
        enhanced = final_rgb.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=2))
        
        # Save as 1000x1000 JPEG with 98% quality
        enhanced.save(dst_path, "JPEG", quality=98, subsampling=0)
        return True
    except Exception as e:
        print(f"Error creating 1000x1000 card for {src_path}: {e}")
        return False

def run():
    blogs = Blog.objects.all().order_by('id')
    print(f"Processing 1000x1000 HD cover images for all {blogs.count()} blogs...")
    
    success_count = 0
    for idx, b in enumerate(blogs, 1):
        filename = os.path.basename(b.image.name) if b.image else f"blog_{b.id}.jpg"
        
        # Check raw image source first, then existing blog image, then media fallback
        possible_sources = [
            os.path.join(MEDIA_BLOGS_DIR, f"raw_{filename}"),
            os.path.join(MEDIA_BLOGS_DIR, filename),
            os.path.join('media', 'products', filename),
            b.image.path if b.image and os.path.exists(b.image.path) else ""
        ]
        
        src_path = None
        for path in possible_sources:
            if path and os.path.exists(path) and not path.endswith('.png_hd') and not 'hd_1000x1000' in path:
                src_path = path
                break
                
        if not src_path and b.image and os.path.exists(b.image.path):
            src_path = b.image.path

        if not src_path:
            print(f"[{idx}/60] WARNING: No source image found for Blog {b.id} ({b.name})")
            continue

        clean_name = filename.replace('hd_1000x1000_', '')
        hd_filename = f"hd_1000x1000_{clean_name}"
        if not hd_filename.lower().endswith(('.jpg', '.jpeg')):
            hd_filename = os.path.splitext(hd_filename)[0] + '.jpg'
            
        dst_path = os.path.join(MEDIA_BLOGS_DIR, hd_filename)
        
        ok = create_1000x1000_card(src_path, dst_path)
        if ok:
            db_rel_path = f"blogs/{hd_filename}"
            b.image = db_rel_path
            b.save()
            
            # Verify dimensions of saved image
            with Image.open(dst_path) as check_img:
                w, h = check_img.size
            print(f"[{idx}/60] SUCCESS: Blog ID {b.id} ({b.name}) -> {db_rel_path} [{w}x{h}px]")
            success_count += 1
            
    print(f"\nCOMPLETED! Upgraded {success_count}/{blogs.count()} blog cover images to 1000x1000 HD!")

if __name__ == '__main__':
    run()
