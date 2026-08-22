import os
import sys
import urllib.request
import re
import django
from PIL import Image, ImageFilter

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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Explicit high-res picture candidate patterns for each model
HIGH_RES_MAP = {
    # iPhones
    "iphone-13-mini-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-mini-01.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-mini-1.jpg"],
    "iphone-13-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-01.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-1.jpg"],
    "iphone-13-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-1.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-01.jpg"],
    "iphone-13-pro-max-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-max-1.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-max-01.jpg"],
    "iphone-14-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-1.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-01.jpg"],
    "iphone-14-plus-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-plus-1.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-plus-01.jpg"],
    "iphone-14-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-1.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-01.jpg"],
    "iphone-14-pro-max-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-max-1.jpg"],
    "iphone-15-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-1.jpg", "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-01.jpg"],
    "iphone-15-plus-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-plus-1.jpg"],
    "iphone-15-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-1.jpg"],
    "iphone-15-pro-max-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"],
    "iphone-16-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-1.jpg"],
    "iphone-16-plus-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-plus-1.jpg"],
    "iphone-16-pro-max-specifications": ["https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-pro-max-1.jpg"],

    # OPPO
    "oppo-find-n3-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-n3-1.jpg"],
    "oppo-find-n3-flip-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-n3-flip-1.jpg"],
    "oppo-find-x8-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x8-pro-1.jpg"],
    "oppo-find-x7-ultra-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x7-ultra-1.jpg"],
    "oppo-find-x7-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x7-1.jpg"],
    "oppo-find-x6-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x6-pro-1.jpg"],
    "oppo-reno-12-pro-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno12-pro-cn-1.jpg", "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno12-pro-1.jpg"],
    "oppo-reno-12-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno12-1.jpg"],
    "oppo-reno-11-pro-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno11-pro-china-1.jpg", "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno11-pro-1.jpg"],
    "oppo-reno-11-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno11-1.jpg"],
    "oppo-reno-10-pro-plus-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno10-pro-plus-1.jpg"],
    "oppo-a3-pro-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a3-pro-1.jpg"],
    "oppo-a98-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a98-1.jpg"],
    "oppo-a79-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a79-1.jpg"],
    "oppo-a58-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a58-4g-1.jpg"],

    # Vivo
    "vivo-x-fold3-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x-fold3-pro-1.jpg"],
    "vivo-x100-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x100-pro-1.jpg"],
    "vivo-x100-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x100-1.jpg"],
    "vivo-x90-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x90-pro-1.jpg"],
    "vivo-v30-pro-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-pro-1.jpg"],
    "vivo-v30-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-lite-1.jpg", "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-1.jpg"],
    "vivo-v29-pro-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v29-pro-1.jpg"],
    "vivo-v29e-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v29e-1.jpg"],
    "vivo-v27-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v27-1.jpg"],
    "vivo-y200e-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y200e-1.jpg"],
    "vivo-y100-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y100-5g-indonesia-1.jpg", "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y100-1.jpg"],
    "vivo-y36-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y36-5g-1.jpg", "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y36-1.jpg"],
    "vivo-y27-5g-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y27-5g-1.jpg", "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y27-1.jpg"],
    "vivo-y17s-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y17s-1.jpg"],
    "vivo-y03-specifications": ["https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y03-1.jpg"],

    # HUAWEI
    "huawei-mate-xt-ultimate-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-mate-xt-ultimate-1.jpg"],
    "huawei-pura-70-ultra-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-pura70-ultra-1.jpg"],
    "huawei-pura-70-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-pura70-pro-1.jpg"],
    "huawei-pura-70-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-pura70-1.jpg"],
    "huawei-mate-60-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-mate-60-pro-1.jpg"],
    "huawei-mate-60-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-mate-60-1.jpg"],
    "huawei-mate-x5-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-mate-x5-1.jpg"],
    "huawei-p60-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-p60-pro-1.jpg"],
    "huawei-p60-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-p60-1.jpg"],
    "huawei-nova-12-pro-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-nova-12-pro-1.jpg"],
    "huawei-nova-12s-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-nova-12s-1.jpg"],
    "huawei-nova-11i-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-nova-11i-1.jpg"],
    "huawei-nova-y91-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-nova-y91-1.jpg"],
    "huawei-nova-y71-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-nova-y71-1.jpg"],
    "huawei-pocket-s-specifications": ["https://fdn2.gsmarena.com/vv/pics/huawei/huawei-pocket-s-1.jpg"]
}

def try_fetch_highres(urls, save_path):
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                if resp.status == 200:
                    with open(save_path, 'wb') as f:
                        f.write(resp.read())
                    return True
        except Exception:
            pass
    return False

def make_ultra_hd_card(src_path, dst_path):
    try:
        orig = Image.open(src_path).convert("RGBA")
        
        # 1. 1000x1000 High-Res Canvas
        W, H = 1000, 1000
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        
        o_w, o_h = orig.size
        # Margin 60px -> inner box 880x880 px
        max_w, max_h = 880, 880
        ratio = min(max_w / o_w, max_h / o_h)
        
        new_w = max(1, int(o_w * ratio))
        new_h = max(1, int(o_h * ratio))
        
        # 2. Resampling with Lanczos
        resized = orig.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        pos_x = (W - new_w) // 2
        pos_y = (H - new_h) // 2
        
        canvas.paste(resized, (pos_x, pos_y), resized)
        
        final_rgb = canvas.convert("RGB")
        
        # 3. UnsharpMask for ultra sharpness
        sharpened = final_rgb.filter(ImageFilter.UnsharpMask(radius=1.5, percent=140, threshold=1))
        
        # Save 1000x1000 with quality 98
        sharpened.save(dst_path, "JPEG", quality=98, subsampling=0)
        return True
    except Exception as e:
        print(f"Error making ultra HD card for {src_path}: {e}")
        return False

def run():
    blogs = Blog.objects.all().order_by('id')
    print(f"Upgrading all {blogs.count()} blogs to TRUE ULTRA-HD 1000x1000 images...")
    
    success_count = 0
    for idx, b in enumerate(blogs, 1):
        clean_slug = b.slug
        candidate_urls = HIGH_RES_MAP.get(clean_slug, [])
        
        raw_hd_path = os.path.join(MEDIA_BLOGS_DIR, f"ultra_raw_{clean_slug}.jpg")
        hd_dst_path = os.path.join(MEDIA_BLOGS_DIR, f"ultra_hd_1000_{clean_slug}.jpg")
        
        fetched = try_fetch_highres(candidate_urls, raw_hd_path)
        src_path = raw_hd_path if fetched else (b.image.path if b.image and os.path.exists(b.image.path) else None)
        
        if not src_path or not os.path.exists(src_path):
            print(f"[{idx}/60] WARNING: Could not find high-res source for {b.name}")
            continue
            
        ok = make_ultra_hd_card(src_path, hd_dst_path)
        if ok:
            db_rel_path = f"blogs/ultra_hd_1000_{clean_slug}.jpg"
            b.image = db_rel_path
            b.save()
            with Image.open(hd_dst_path) as chk:
                w, h = chk.size
            print(f"[{idx}/60] ULTRA-HD OK: Blog ID {b.id} ({b.name}) -> {db_rel_path} [{w}x{h}px] (Source fetched: {fetched})")
            success_count += 1
            
    print(f"\nFINISH! Successfully upgraded {success_count}/{blogs.count()} blogs to TRUE ULTRA-HD 1000x1000 images!")

if __name__ == '__main__':
    run()
