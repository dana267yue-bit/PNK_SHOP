import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Category, Product

print("--- ALL CATEGORIES ---")
for c in Category.objects.all():
    count = Product.objects.filter(category=c).count()
    print(f"Category ID: {c.id}, Name: '{c.name}', Product Count: {count}")

print("\n--- PRODUCTS IN ACCESSORY CATEGORY (ID=2) ---")
acc_products = Product.objects.filter(category_id=2)
for p in acc_products[:20]:
    print(f"ID: {p.id}, Name: '{p.name}', Brand: '{p.brand.name if p.brand else None}'")

print("\n--- PRODUCTS IN SMARTPHONE CATEGORY (ID=1) ---")
phone_products = Product.objects.filter(category_id=1)
for p in phone_products[:10]:
    print(f"ID: {p.id}, Name: '{p.name}', Brand: '{p.brand.name if p.brand else None}'")
