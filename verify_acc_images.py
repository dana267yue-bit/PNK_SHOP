import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product
from django.conf import settings

missing = 0
for p in Product.objects.filter(category_id=2):
    full_path = os.path.join(settings.MEDIA_ROOT, p.image.name) if p.image else ""
    exists = os.path.exists(full_path)
    if not exists:
        missing += 1
        print(f"MISSING IMAGE: ID {p.id} - {p.name} ({p.image.name if p.image else 'None'})")

print(f"Checked 40 accessories. Missing images count: {missing}")
