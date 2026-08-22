import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product

image_mapping = {
    # Apple Accessories
    "Apple MagSafe Charger (25W)": "products/magsafe_charger.jpg",
    "Apple AirTag (1 Pack)": "products/airtags.jpg",
    "AirPods Pro (2nd Gen) USB-C": "products/beats_earbuds.jpg",
    "Belkin BoostCharge Pro 3-in-1 MagSafe Charger": "products/belkin_3in1.jpg",
    "Apple 20W USB-C Power Adapter": "products/apple2.jpeg",
    "iPhone 15 Pro Max Clear Case with MagSafe": "products/apple3.jpg",
    "iPhone 15 Silicone Case with MagSafe (Black)": "products/apple4.jpg",
    "Apple FineWoven Wallet with MagSafe": "products/apple5.jpg",
    "Apple USB-C to Lightning Cable (1m)": "products/apple8.jpg",
    "Apple USB-C Woven Charge Cable (60W 1m)": "products/apple9.jpg",

    # OPPO Accessories
    "OPPO SUPERVOOC 80W Power Adapter": "products/oppo1.jpg",
    "OPPO Enco Air3 Pro Wireless Earbuds": "products/oppo2.jpg",
    "OPPO Enco X2 Noise Cancelling Earbuds": "products/oppo3.jpg",
    "OPPO Reno11 Pro Magnetic Protective Case": "products/OppoA3x-Purple.jpg",
    "OPPO Find X7 Ultra Premium Leather Case": "products/oppo1.jpg",
    "OPPO 67W SUPERVOOC Car Charger": "products/oppo2.jpg",
    "OPPO Type-C Fast Charging Cable (8A 1m)": "products/oppo3.jpg",
    "OPPO AirVOOC 50W Wireless Charger Stand": "products/OppoA3x-Purple.jpg",
    "OPPO Pad 2 Smart Touch Keyboard Case": "products/oppo1.jpg",
    "OPPO Band 2 Fitness Tracker": "products/oppo2.jpg",

    # Vivo Accessories
    "Vivo 120W FlashCharge Power Adapter": "products/vivo1.jpg",
    "Vivo TWS 3 Pro True Wireless Earphones": "products/vivo4.jpg",
    "Vivo V30 Pro Anti-Drop Armor Case": "products/Vivo_V29e.jpg",
    "Vivo X100 Pro Photography Grip Kit & Case": "products/vivoX100.jpg",
    "Vivo 80W FlashCharge Car Charger": "products/vivoY03T.jpg",
    "Vivo 6A Type-C Super Fast Cable (1.2m)": "products/vivo1.jpg",
    "Vivo 50W Wireless FlashCharger Stand": "products/vivo4.jpg",
    "Vivo TWS Air2 Lightweight Bluetooth Earbuds": "products/Vivo_V29e.jpg",
    "Vivo X Fold3 Pro Carbon Fiber Case": "products/vivoX100.jpg",
    "Vivo Watch 3 Smartwatch (Sport Edition)": "products/vivoY03T.jpg",

    # Huawei Accessories
    "Huawei SuperCharge 88W Max Power Adapter": "products/huawei_P20.jpg",
    "Huawei FreeBuds Pro 3 ANC Earbuds": "products/nova14i.webp",
    "Huawei FreeBuds 5i Hi-Res Wireless Earbuds": "products/huawei_P20.jpg",
    "Huawei Mate 60 Pro Magnetic Ring Case": "products/nova14i.webp",
    "Huawei Mate X5 Kevlar Protective Cover": "products/huawei_P20.jpg",
    "Huawei 50W SuperCharge Wireless Car Charger": "products/nova14i.webp",
    "Huawei 6A Type-C SuperCharge Cable (1.5m)": "products/huawei_P20.jpg",
    "Huawei SuperCharge 50W Vertical Charger Stand": "products/nova14i.webp",
    "Huawei M-Pencil (3rd Gen) NearLink Stylus": "products/huawei_P20.jpg",
    "Huawei Band 9 Fitness Smart Tracker": "products/nova14i.webp",
}

updated_count = 0
for name, img_path in image_mapping.items():
    res = Product.objects.filter(name=name).update(image=img_path)
    if res > 0:
        updated_count += 1

print(f"Updated images for {updated_count} accessory products!")
