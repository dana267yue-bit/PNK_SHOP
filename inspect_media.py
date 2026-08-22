import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product
from django.conf import settings

print("MEDIA_ROOT:", settings.MEDIA_ROOT)
if os.path.exists(settings.MEDIA_ROOT):
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        print(root, files[:5])

print("\nSample Product images:")
for p in Product.objects.all()[:10]:
    print(p.name, "->", p.image.name if p.image else "No image")
