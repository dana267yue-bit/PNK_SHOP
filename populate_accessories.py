import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Category, Brand, Product

# Fetch category 'Accessory'
accessory_cat = Category.objects.get(id=2) # Accessory

# Fetch brands
apple_brand = Brand.objects.get(id=5) # apple
oppo_brand = Brand.objects.get(id=3) # oppo
vivo_brand = Brand.objects.get(id=1) # vivo
huawei_brand = Brand.objects.get(id=4) # huawei

accessories_data = [
    # --- APPLE / IPHONE ACCESSORIES (10 items) ---
    {
        "name": "Apple MagSafe Charger (25W)",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 39.00,
        "old_price": 49.00,
        "stock": 25,
        "promotion": "Hot Item",
        "description": "ឆ្នាំងសាកឥតខ្សែ Apple MagSafe Charger 25W សាកលឿន និងមានសុវត្ថិភាពខ្ពស់សម្រាប់ iPhone 12/13/14/15 Series។",
        "image": "products/apple1.jpg"
    },
    {
        "name": "Apple 20W USB-C Power Adapter",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 19.00,
        "old_price": 25.00,
        "stock": 50,
        "promotion": "Best Seller",
        "description": "ក្បាលសាកលឿន Original Apple 20W USB-C Power Adapter សម្រាប់ iPhone និង iPad។",
        "image": "products/apple2.jpeg"
    },
    {
        "name": "AirPods Pro (2nd Gen) USB-C",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 249.00,
        "old_price": 269.00,
        "stock": 15,
        "promotion": "Special Discount",
        "description": "កាសឥតខ្សែ AirPods Pro 2 ជាមួយប្រព័ន្ធកាត់បន្ថយសំឡេងរំខាន Active Noise Cancellation និងរន្ធសាក USB-C។",
        "image": "products/apple10.jpg"
    },
    {
        "name": "iPhone 15 Pro Max Clear Case with MagSafe",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 49.00,
        "old_price": 59.00,
        "stock": 30,
        "promotion": "New Arrival",
        "description": "ស្រោមការពារថ្លា iPhone 15 Pro Max ការពារជម្រុះ និងទ្រទ្រង់ការសាក MagSafe យ៉ាងរហ័ស។",
        "image": "products/apple11.jpg"
    },
    {
        "name": "iPhone 15 Silicone Case with MagSafe (Black)",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 45.00,
        "old_price": 55.00,
        "stock": 20,
        "promotion": "Popular",
        "description": "ស្រោម Silicone ការពារ iPhone 15 ផ្ទៃទន់រលោង កាន់ណែនដៃ និងគាំទ្រ MagSafe។",
        "image": "products/apple12.jpg"
    },
    {
        "name": "Apple FineWoven Wallet with MagSafe",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 59.00,
        "old_price": 69.00,
        "stock": 18,
        "promotion": "Premium",
        "description": "កាបូបស្បែកបិទខ្នង iPhone Apple FineWoven Wallet សម្រាប់ដាក់កាតធនាគារ និងអត្តសញ្ញាណប័ណ្ណ។",
        "image": "products/apple1.jpg"
    },
    {
        "name": "Apple USB-C to Lightning Cable (1m)",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 19.00,
        "old_price": 25.00,
        "stock": 40,
        "promotion": "Essential",
        "description": "ខ្សែសាកលឿន Original Apple USB-C to Lightning ប្រវែង 1 ម៉ែត្រ។",
        "image": "products/apple2.jpeg"
    },
    {
        "name": "Apple USB-C Woven Charge Cable (60W 1m)",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 19.00,
        "old_price": 25.00,
        "stock": 35,
        "promotion": "Durable",
        "description": "ខ្សែសាកប្រ៊ែដស្បៃ Apple USB-C Woven Cable 60W កម្លាំងសាកខ្លាំង និងធន់មាំ។",
        "image": "products/apple10.jpg"
    },
    {
        "name": "Apple AirTag (1 Pack)",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 29.00,
        "old_price": 35.00,
        "stock": 40,
        "promotion": "Smart Tracking",
        "description": "ឧបករណ៍ស្វែងរកសម្ភារៈ Apple AirTag ភ្ជាប់ជាមួយកម្មវិធី Find My យ៉ាងងាយស្រួល។",
        "image": "products/apple11.jpg"
    },
    {
        "name": "Belkin BoostCharge Pro 3-in-1 MagSafe Charger",
        "brand": apple_brand,
        "category": accessory_cat,
        "price": 149.00,
        "old_price": 169.00,
        "stock": 12,
        "promotion": "3-in-1 Charger",
        "description": "ជើងសាកឥតខ្សែ 3-in-1 សម្រាប់ iPhone, Apple Watch និង AirPods ក្នុងពេលតែមួយ។",
        "image": "products/apple12.jpg"
    },

    # --- OPPO ACCESSORIES (10 items) ---
    {
        "name": "OPPO SUPERVOOC 80W Power Adapter",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 35.00,
        "old_price": 45.00,
        "stock": 30,
        "promotion": "Flash Charge",
        "description": "ក្បាលសាកលឿនបំផុត OPPO SUPERVOOC 80W មិនក្តៅម៉ាស៊ីន និងមានសុវត្ថិភាព។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "OPPO Enco Air3 Pro Wireless Earbuds",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 69.00,
        "old_price": 79.00,
        "stock": 25,
        "promotion": "Hi-Res Audio",
        "description": "កាសឥតខ្សែ OPPO Enco Air3 Pro សំឡេងច្បាស់ល្អ ជាមួយបច្ចេកវិទ្យាកាត់សំឡេង ANC។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "OPPO Enco X2 Noise Cancelling Earbuds",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 129.00,
        "old_price": 149.00,
        "stock": 15,
        "promotion": "Flagship Sound",
        "description": "កាសកំពូល OPPO Enco X2 រចនាដោយ Dynaudio សំឡេងបាសធ្ងន់ និងច្បាស់ល្អឥតខ្ចោះ។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "OPPO Reno11 Pro Magnetic Protective Case",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 18.00,
        "old_price": 25.00,
        "stock": 40,
        "promotion": "Slim Protection",
        "description": "ស្រោមការពារ OPPO Reno11 Pro ស្តើង ស្អាត ការពារជ្រុង និងកាមេរ៉ា។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "OPPO Find X7 Ultra Premium Leather Case",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 29.00,
        "old_price": 39.00,
        "stock": 20,
        "promotion": "Luxury Leather",
        "description": "ស្រោមស្បែកខ្ពស់ OPPO Find X7 Ultra បង្កើនភាពប្រណីត និងសោភ័ណភាព។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "OPPO 67W SUPERVOOC Car Charger",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 25.00,
        "old_price": 32.00,
        "stock": 25,
        "promotion": "Car Charger",
        "description": "ឆ្នាំងសាកក្នុងរថយន្ត OPPO 67W SUPERVOOC សាកលឿនទាន់ចិត្តពេលធ្វើដំណើរ។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "OPPO Type-C Fast Charging Cable (8A 1m)",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 12.00,
        "old_price": 18.00,
        "stock": 50,
        "promotion": "8A Cable",
        "description": "ខ្សែសាកល្បឿនលឿន OPPO Type-C 8A ទ្រទ្រង់ SUPERVOOC សាកលឿន។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "OPPO AirVOOC 50W Wireless Charger Stand",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 59.00,
        "old_price": 69.00,
        "stock": 15,
        "promotion": "50W Wireless",
        "description": "ជើងសាកឥតខ្សែ OPPO AirVOOC 50W ជាមួយកង្ហារត្រជាក់កាត់បន្ថយកំដៅ។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "OPPO Pad 2 Smart Touch Keyboard Case",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 89.00,
        "old_price": 109.00,
        "stock": 10,
        "promotion": "Smart Keyboard",
        "description": "ក្ដារចុចស្មាតសម្រាប់ OPPO Pad 2 វាយអក្សររហ័ស ជាមួយ Touchpad។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "OPPO Band 2 Fitness Tracker",
        "brand": oppo_brand,
        "category": accessory_cat,
        "price": 49.00,
        "old_price": 59.00,
        "stock": 30,
        "promotion": "Fitness Tracker",
        "description": "នាឡិកាសុខភាព OPPO Band 2 វាស់ចង្វាក់បេះដូង និងកម្រិតអុកស៊ីសែនក្នុងឈាម។",
        "image": "products/A3x_V4QY6zh.PNG"
    },

    # --- VIVO ACCESSORIES (10 items) ---
    {
        "name": "Vivo 120W FlashCharge Power Adapter",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 45.00,
        "old_price": 55.00,
        "stock": 25,
        "promotion": "Super Fast",
        "description": "ក្បាលសាកលឿនរហ័ស Vivo 120W FlashCharge សាកពេញក្នុងរយៈពេលខ្លី។",
        "image": "products/apple1.jpg"
    },
    {
        "name": "Vivo TWS 3 Pro True Wireless Earphones",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 99.00,
        "old_price": 119.00,
        "stock": 20,
        "promotion": "Hi-Fi Sound",
        "description": "កាសឥតខ្សែ Vivo TWS 3 Pro គាំទ្រសំឡេង Hi-Fi និងប្រព័ន្ធ ANC 49dB។",
        "image": "products/apple2.jpeg"
    },
    {
        "name": "Vivo V30 Pro Anti-Drop Armor Case",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 15.00,
        "old_price": 22.00,
        "stock": 35,
        "promotion": "Armor Shield",
        "description": "ស្រោមការពារជ្រុង Vivo V30 Pro រចនារឹងមាំ ការពារការទង្គិច និងជម្រុះ។",
        "image": "products/apple10.jpg"
    },
    {
        "name": "Vivo X100 Pro Photography Grip Kit & Case",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 49.00,
        "old_price": 65.00,
        "stock": 15,
        "promotion": "Camera Grip",
        "description": "ឈុតដៃកាន់ថតរូប និងស្រោមការពារ Vivo X100 Pro សម្រាប់អ្នកស្រឡាញ់ការថតរូប។",
        "image": "products/apple11.jpg"
    },
    {
        "name": "Vivo 80W FlashCharge Car Charger",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 29.00,
        "old_price": 38.00,
        "stock": 25,
        "promotion": "Car Charger",
        "description": "ឆ្នាំងសាកឡាន Vivo 80W FlashCharge សាកបាន ២ ឧបករណ៍ក្នុងពេលតែមួយ។",
        "image": "products/apple12.jpg"
    },
    {
        "name": "Vivo 6A Type-C Super Fast Cable (1.2m)",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 14.00,
        "old_price": 19.00,
        "stock": 60,
        "promotion": "6A Cable",
        "description": "ខ្សែសាកលឿន Vivo 6A Type-C ប្រវែង 1.2m ស្បែកខ្សែកាបស្កត់ស្ទាយមាំ។",
        "image": "products/apple1.jpg"
    },
    {
        "name": "Vivo 50W Wireless FlashCharger Stand",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 65.00,
        "old_price": 79.00,
        "stock": 12,
        "promotion": "50W Wireless",
        "description": "ជើងសាកឥតខ្សែ Vivo 50W Wireless FlashCharger រចនាបញ្ឈរ ងាយស្រួលមើលអេក្រង់។",
        "image": "products/apple2.jpeg"
    },
    {
        "name": "Vivo TWS Air2 Lightweight Bluetooth Earbuds",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 39.00,
        "old_price": 49.00,
        "stock": 30,
        "promotion": "Ultra Light",
        "description": "កាសឥតខ្សែទម្ងន់ស្រាល Vivo TWS Air2 ពាក់ស្រួលត្រចៀក និងបាសបុកពីរោះ។",
        "image": "products/apple10.jpg"
    },
    {
        "name": "Vivo X Fold3 Pro Carbon Fiber Case",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 35.00,
        "old_price": 45.00,
        "stock": 15,
        "promotion": "Carbon Fiber",
        "description": "ស្រោមការពារកាបូនហ្វាយប៊័រ Vivo X Fold3 Pro ស្តើង ស្រាល និងការពារបានល្អ។",
        "image": "products/apple11.jpg"
    },
    {
        "name": "Vivo Watch 3 Smartwatch (Sport Edition)",
        "brand": vivo_brand,
        "category": accessory_cat,
        "price": 139.00,
        "old_price": 159.00,
        "stock": 10,
        "promotion": "Smartwatch",
        "description": "នាឡិកាឆ្លាតវៃ Vivo Watch 3 ប្រព័ន្ធប្រតិបត្តិការ BlueOS និងថ្មប្រើបានយូរ។",
        "image": "products/apple12.jpg"
    },

    # --- HUAWEI ACCESSORIES (10 items) ---
    {
        "name": "Huawei SuperCharge 88W Max Power Adapter",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 42.00,
        "old_price": 52.00,
        "stock": 30,
        "promotion": "88W Max",
        "description": "ក្បាលសាកលឿនកំពូល Huawei 88W SuperCharge មានរន្ធ USB-A និង USB-C។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "Huawei FreeBuds Pro 3 ANC Earbuds",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 179.00,
        "old_price": 199.00,
        "stock": 18,
        "promotion": "Dual-Driver",
        "description": "កាសឥតខ្សែប្រណីត Huawei FreeBuds Pro 3 សំឡេងកម្រិតស្ទូឌីយោ និង ANC 3.0។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "Huawei FreeBuds 5i Hi-Res Wireless Earbuds",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 79.00,
        "old_price": 89.00,
        "stock": 25,
        "promotion": "Hi-Res ANC",
        "description": "កាសឥតខ្សែ Huawei FreeBuds 5i កាត់សំឡេងរំខាន 42dB ថ្មប្រើបាន 28 ម៉ោង។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "Huawei Mate 60 Pro Magnetic Ring Case",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 22.00,
        "old_price": 29.00,
        "stock": 40,
        "promotion": "Ring Case",
        "description": "ស្រោមការពារ Huawei Mate 60 Pro មានកងដែកទប់ដៃ និងគាំទ្រជើងសាក MagSafe/Wireless។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "Huawei Mate X5 Kevlar Protective Cover",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 45.00,
        "old_price": 59.00,
        "stock": 15,
        "promotion": "Kevlar Shield",
        "description": "ស្រោមការពារកម្រិតខ្ពស់ Huawei Mate X5 ធ្វើពីសរសៃ Kevlar ស្មិតមាំខ្លាំង។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "Huawei 50W SuperCharge Wireless Car Charger",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 55.00,
        "old_price": 68.00,
        "stock": 20,
        "promotion": "50W Wireless Car",
        "description": "ជើងសាកឥតខ្សែក្នុងរថយន្ត Huawei 50W មានសេនស័របើកបិទដៃស្វ័យប្រវត្តិ។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "Huawei 6A Type-C SuperCharge Cable (1.5m)",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 15.00,
        "old_price": 22.00,
        "stock": 50,
        "promotion": "Super Cable",
        "description": "ខ្សែសាកដើម Huawei 6A Type-C 1.5m ផ្ទេរទិន្នន័យលឿន និងសាកភ្លើងខ្លាំង។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "Huawei SuperCharge 50W Vertical Charger Stand",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 59.00,
        "old_price": 72.00,
        "stock": 15,
        "promotion": "Vertical Stand",
        "description": "ជើងសាកឥតខ្សែ 50W សម្រាប់ Huawei Mate & P Series ជាមួយកង្ហារត្រជាក់ស្ងាត់។",
        "image": "products/A3x_V4QY6zh.PNG"
    },
    {
        "name": "Huawei M-Pencil (3rd Gen) NearLink Stylus",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 99.00,
        "old_price": 119.00,
        "stock": 12,
        "promotion": "NearLink Tech",
        "description": "ប៊ិចគូរ M-Pencil ជំនាន់ទី 3 គាំទ្រ NearLink ភាពត្រឹមត្រូវខ្ពស់ 10,000+ កម្រិតសម្ពាធ។",
        "image": "products/A3x.PNG"
    },
    {
        "name": "Huawei Band 9 Fitness Smart Tracker",
        "brand": huawei_brand,
        "category": accessory_cat,
        "price": 45.00,
        "old_price": 55.00,
        "stock": 30,
        "promotion": "Fitness Smart Band",
        "description": "នាឡិកាសុខភាព Huawei Band 9 អេក្រង់ AMOLED ស្អាត តាមដានដំណេក TruSleep 4.0។",
        "image": "products/A3x_V4QY6zh.PNG"
    }
]

created_count = 0
updated_count = 0

for item in accessories_data:
    product, created = Product.objects.update_or_create(
        name=item["name"],
        brand=item["brand"],
        defaults={
            "category": item["category"],
            "price": item["price"],
            "old_price": item["old_price"],
            "stock": item["stock"],
            "promotion": item["promotion"],
            "description": item["description"],
            "image": item["image"],
            "status": "Pending"
        }
    )
    if created:
        created_count += 1
    else:
        updated_count += 1

print(f"Successfully processed {len(accessories_data)} accessories!")
print(f"Created new: {created_count}, Updated existing: {updated_count}")
