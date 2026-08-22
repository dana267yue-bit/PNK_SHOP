import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Category, Brand
from django.conf import settings

brands_dir = settings.MEDIA_ROOT / 'brands'
cats_dir = settings.MEDIA_ROOT / 'categories'
os.makedirs(brands_dir, exist_ok=True)
os.makedirs(cats_dir, exist_ok=True)

# Transparent SVG Definitions for Brands
brand_svgs = {
    'apple': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <path d="M66.4 53.3c.1 8.8 7.7 11.7 7.8 11.8-.1.2-1.2 4.2-4.1 8.4-2.5 3.6-5.1 7.2-9.1 7.3-3.9.1-5.2-2.3-9.7-2.3-4.5 0-5.9 2.2-9.6 2.4-3.9.1-6.9-3.9-9.4-7.5-5.1-7.4-9-20.9-3.8-30 2.6-4.5 7.2-7.4 12.2-7.5 3.8-.1 7.5 2.6 9.8 2.6 2.3 0 6.7-3.2 11.2-2.7 1.9.1 7.2.8 10.6 5.7-.3.2-6.3 3.7-6.2 11.8zM57.6 30c2.1-2.5 3.5-6 3.1-9.5-3 1.2-6.6 3.1-8.7 5.6-1.9 2.2-3.6 5.8-3.1 9.2 3.3.3 6.6-2.8 8.7-5.3z" fill="#0f172a"/>
</svg>''',

    'samsung': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" width="120" height="60">
  <text x="60" y="40" font-family="'Segoe UI', sans-serif" font-weight="900" font-size="22" fill="#034EA2" text-anchor="middle" letter-spacing="1">SAMSUNG</text>
</svg>''',

    'huawei': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <g transform="translate(50, 50) scale(0.9)">
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(45)"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(-45)"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(90)"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(-90)"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(135)"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(-135)"/>
    <path d="M0 -35 C5 -20, 5 -10, 0 0 C-5 -10, -5 -20, 0 -35" fill="#ED1C24" transform="rotate(180)"/>
  </g>
</svg>''',

    'oppo': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 60" width="100" height="60">
  <text x="50" y="42" font-family="'Segoe UI', sans-serif" font-weight="bold" font-size="34" fill="#008B5E" text-anchor="middle" letter-spacing="-1">oppo</text>
</svg>''',

    'vivo': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 60" width="100" height="60">
  <text x="50" y="44" font-family="'Segoe UI', sans-serif" font-weight="bold" font-style="italic" font-size="36" fill="#415FFF" text-anchor="middle" letter-spacing="-1">vivo</text>
</svg>''',

    'xiaomi': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 60" width="100" height="60">
  <rect x="25" y="10" width="50" height="40" rx="10" fill="#FF6900"/>
  <path d="M38 22 h8 v16 h-8 z M50 22 h12 v16 h-4 v-10 h-4 v10 h-4 z" fill="#ffffff"/>
</svg>''',

    'realme': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" width="120" height="60">
  <rect x="10" y="15" width="100" height="30" rx="4" fill="#FFC900"/>
  <text x="60" y="36" font-family="'Segoe UI', sans-serif" font-weight="bold" font-size="18" fill="#000000" text-anchor="middle">realme</text>
</svg>''',
}

# Transparent SVG Definitions for Categories
cat_svgs = {
    'all': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <rect x="15" y="15" width="30" height="30" rx="6" fill="#10B981"/>
  <rect x="55" y="15" width="30" height="30" rx="6" fill="#10B981"/>
  <rect x="15" y="55" width="30" height="30" rx="6" fill="#10B981"/>
  <rect x="55" y="55" width="30" height="30" rx="6" fill="#10B981"/>
</svg>''',

    'smartphone': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <rect x="28" y="12" width="44" height="76" rx="8" fill="none" stroke="#10B981" stroke-width="6"/>
  <rect x="34" y="22" width="32" height="52" rx="3" fill="#10B981"/>
  <circle cx="50" cy="80" r="3" fill="#10B981"/>
</svg>''',

    'accessory': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <path d="M25 50 C25 28, 75 28, 75 50 M25 50 L25 68 C25 72, 30 75, 35 75 L38 75 C42 75, 45 72, 45 68 L45 50 Z M75 50 L75 68 C75 72, 70 75, 65 75 L62 75 C58 75, 55 72, 55 68 L55 50 Z" stroke="#10B981" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
}

for name, content in brand_svgs.items():
    file_path = os.path.join(brands_dir, f'{name}.svg')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for name, content in cat_svgs.items():
    file_path = os.path.join(cats_dir, f'{name}.svg')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for b_name in brand_svgs.keys():
    brand = Brand.objects.filter(name__iexact=b_name).first()
    if brand:
        brand.logo = f'brands/{b_name}.svg'
        brand.save()

cat_phone = Category.objects.filter(name__iexact='smartphone').first()
if cat_phone:
    cat_phone.image = 'categories/smartphone.svg'
    cat_phone.save()

cat_acc = Category.objects.filter(name__iexact='accessory').first()
if cat_acc:
    cat_acc.image = 'categories/accessory.svg'
    cat_acc.save()

print('All brand and category transparent SVGs updated successfully!')
