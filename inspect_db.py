import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Category, Brand, Product

print("--- CATEGORIES ---")
for c in Category.objects.all():
    print(f"ID: {c.id}, Name: '{c.name}', Slug: '{c.slug}'")

print("\n--- BRANDS ---")
for b in Brand.objects.all():
    print(f"ID: {b.id}, Name: '{b.name}'")
