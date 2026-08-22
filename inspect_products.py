import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product

print("Distinct statuses:", set(Product.objects.values_list('status', flat=True)))
print("Sample product status & details:")
for p in Product.objects.all()[:5]:
    print(f"ID: {p.id}, Name: {p.name}, Price: {p.price}, Status: '{p.status}'")
