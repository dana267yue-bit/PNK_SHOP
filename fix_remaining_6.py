import os
import urllib.request
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product
from django.conf import settings

media_products_dir = os.path.join(settings.MEDIA_ROOT, 'products')

remaining_6 = {
    "Apple MagSafe Charger (25W)": {
        "filename": "apple_magsafe_25w_v2.jpg",
        "url": "https://images.unsplash.com/photo-1616348436168-de43ad0db179?q=80&w=800&auto=format&fit=crop"
    },
    "Apple AirTag (1 Pack)": {
        "filename": "apple_airtag_v2.jpg",
        "url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO AirVOOC 50W Wireless Charger Stand": {
        "filename": "oppo_50w_stand_v2.jpg",
        "url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo 50W Wireless FlashCharger Stand": {
        "filename": "vivo_50w_stand_v2.jpg",
        "url": "https://images.unsplash.com/photo-1586953208448-b95a79798f07?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei SuperCharge 50W Vertical Charger Stand": {
        "filename": "huawei_50w_stand_v2.jpg",
        "url": "https://images.unsplash.com/photo-1610465299993-e6675c9f9efa?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei M-Pencil (3rd Gen) NearLink Stylus": {
        "filename": "huawei_mpencil_v2.jpg",
        "url": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"
    }
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, item in remaining_6.items():
    file_path = os.path.join(media_products_dir, item["filename"])
    rel_db_path = f"products/{item['filename']}"
    try:
        req = urllib.request.Request(item["url"], headers=headers)
        with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
            out_file.write(response.read())
        Product.objects.filter(name=name).update(image=rel_db_path)
        print(f"Fixed & updated: {name} -> {rel_db_path}")
    except Exception as e:
        print(f"Failed for {name}: {e}")
