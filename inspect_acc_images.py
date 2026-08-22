import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product
from django.conf import settings

print("Products in category Accessory (ID=2):")
for p in Product.objects.filter(category_id=2)[:10]:
    print(f"ID: {p.id}, Name: {p.name}")
    print(f"   Image Field: {p.image.name if p.image else 'NO IMAGE'}")
    if p.image:
        full_path = os.path.join(settings.MEDIA_ROOT, p.image.name)
        print(f"   Full Path Exists?: {os.path.exists(full_path)} ({full_path})")
