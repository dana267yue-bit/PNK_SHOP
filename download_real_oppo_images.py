import os
import urllib.request
import django
import sys
from PIL import Image

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

OPPO_DOWNLOAD_LIST = [
    {
        "name": "OPPO Find N3",
        "slug": "oppo-find-n3-specifications",
        "filename": "oppo_find_n3_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-n3.jpg",
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-n3-fold.jpg"
        ]
    },
    {
        "name": "OPPO Find N3 Flip",
        "slug": "oppo-find-n3-flip-specifications",
        "filename": "oppo_find_n3_flip_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-n3-flip.jpg"
        ]
    },
    {
        "name": "OPPO Find X8 Pro",
        "slug": "oppo-find-x8-pro-specifications",
        "filename": "oppo_find_x8_pro_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x8-pro.jpg"
        ]
    },
    {
        "name": "OPPO Find X7 Ultra",
        "slug": "oppo-find-x7-ultra-specifications",
        "filename": "oppo_find_x7_ultra_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x7-ultra.jpg"
        ]
    },
    {
        "name": "OPPO Find X7",
        "slug": "oppo-find-x7-specifications",
        "filename": "oppo_find_x7_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x7.jpg"
        ]
    },
    {
        "name": "OPPO Find X6 Pro",
        "slug": "oppo-find-x6-pro-specifications",
        "filename": "oppo_find_x6_pro_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-find-x6-pro.jpg"
        ]
    },
    {
        "name": "OPPO Reno 12 Pro 5G",
        "slug": "oppo-reno-12-pro-5g-specifications",
        "filename": "oppo_reno_12_pro_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-pro-cn.jpg",
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12-pro.jpg"
        ]
    },
    {
        "name": "OPPO Reno 12 5G",
        "slug": "oppo-reno-12-5g-specifications",
        "filename": "oppo_reno_12_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno12.jpg"
        ]
    },
    {
        "name": "OPPO Reno 11 Pro 5G",
        "slug": "oppo-reno-11-pro-5g-specifications",
        "filename": "oppo_reno_11_pro_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-pro-china.jpg",
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-pro-cn.jpg"
        ]
    },
    {
        "name": "OPPO Reno 11 5G",
        "slug": "oppo-reno-11-5g-specifications",
        "filename": "oppo_reno_11_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-international.jpg"
        ]
    },
    {
        "name": "OPPO Reno 10 Pro+ 5G",
        "slug": "oppo-reno-10-pro-plus-5g-specifications",
        "filename": "oppo_reno_10_pro_plus_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-reno10-pro-plus.jpg"
        ]
    },
    {
        "name": "OPPO A3 Pro 5G",
        "slug": "oppo-a3-pro-5g-specifications",
        "filename": "oppo_a3_pro_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a3-pro.jpg"
        ]
    },
    {
        "name": "OPPO A98 5G",
        "slug": "oppo-a98-5g-specifications",
        "filename": "oppo_a98_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a98-5g.jpg"
        ]
    },
    {
        "name": "OPPO A79 5G",
        "slug": "oppo-a79-5g-specifications",
        "filename": "oppo_a79_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a79-5g.jpg",
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a79.jpg"
        ]
    },
    {
        "name": "OPPO A58 5G",
        "slug": "oppo-a58-5g-specifications",
        "filename": "oppo_a58_real.jpg",
        "urls": [
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a58-5g.jpg",
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a58-4g.jpg",
            "https://fdn2.gsmarena.com/vv/bigpic/oppo-a58.jpg"
        ]
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def make_clean_card(src_path, dst_path):
    try:
        orig = Image.open(src_path).convert("RGBA")
        W, H = 600, 420
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        
        o_w, o_h = orig.size
        ratio = min((W - 60) / o_w, (H - 40) / o_h)
        new_w = int(o_w * ratio)
        new_h = int(o_h * ratio)
        
        resized = orig.resize((new_w, new_h), Image.Resampling.LANCZOS)
        pos_x = (W - new_w) // 2
        pos_y = (H - new_h) // 2
        
        canvas.paste(resized, (pos_x, pos_y), resized)
        final_rgb = canvas.convert("RGB")
        final_rgb.save(dst_path, "JPEG", quality=98)
        return True
    except Exception as e:
        print(f"Error processing image {src_path}: {e}")
        return False

def try_download(urls, raw_path):
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                if resp.status == 200:
                    with open(raw_path, 'wb') as f:
                        f.write(resp.read())
                    print(f"Downloaded successfully from {url}")
                    return True
        except Exception as e:
            print(f"Failed {url}: {e}")
    return False

def run():
    print("Starting download of real authentic OPPO images...")
    success_count = 0
    
    for idx, item in enumerate(OPPO_DOWNLOAD_LIST, 1):
        raw_path = os.path.join(MEDIA_BLOGS_DIR, f"raw_{item['filename']}")
        card_path = os.path.join(MEDIA_BLOGS_DIR, item['filename'])
        
        downloaded = try_download(item['urls'], raw_path)
        if downloaded:
            processed = make_clean_card(raw_path, card_path)
            if processed:
                db_image_path = f"blogs/{item['filename']}"
                try:
                    blog_obj = Blog.objects.get(slug=item["slug"])
                    blog_obj.image = db_image_path
                    blog_obj.save()
                    print(f"[{idx}/15] UPDATED Blog ID {blog_obj.id}: {blog_obj.name} with real image {db_image_path}")
                    success_count += 1
                except Blog.DoesNotExist:
                    print(f"[{idx}/15] ERROR: Blog with slug {item['slug']} not found in DB!")
        else:
            print(f"[{idx}/15] FAILED to download image for {item['name']}")
            
    print(f"\nCOMPLETED! Updated {success_count}/{len(OPPO_DOWNLOAD_LIST)} OPPO blogs with real images.")

if __name__ == '__main__':
    run()
