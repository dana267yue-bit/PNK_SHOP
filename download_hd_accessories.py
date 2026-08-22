import os
import urllib.request
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
django.setup()

from shop.models import Product
from django.conf import settings

# Directory for downloaded accessory images
media_products_dir = os.path.join(settings.MEDIA_ROOT, 'products')
os.makedirs(media_products_dir, exist_ok=True)

# High Quality HD Image URLs mapped to each accessory product
hd_accessory_images = {
    # --- APPLE ACCESSORIES ---
    "Apple MagSafe Charger (25W)": {
        "filename": "apple_magsafe_25w.jpg",
        "url": "https://images.unsplash.com/photo-1622445268465-8478d058864a?q=80&w=800&auto=format&fit=crop"
    },
    "Apple 20W USB-C Power Adapter": {
        "filename": "apple_20w_adapter.jpg",
        "url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=800&auto=format&fit=crop"
    },
    "AirPods Pro (2nd Gen) USB-C": {
        "filename": "airpods_pro_2.jpg",
        "url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?q=80&w=800&auto=format&fit=crop"
    },
    "iPhone 15 Pro Max Clear Case with MagSafe": {
        "filename": "iphone15_clear_case.jpg",
        "url": "https://images.unsplash.com/photo-1603313011101-320f26a4f6f6?q=80&w=800&auto=format&fit=crop"
    },
    "iPhone 15 Silicone Case with MagSafe (Black)": {
        "filename": "iphone15_silicone_case.jpg",
        "url": "https://images.unsplash.com/photo-1541877944-ac82a091518a?q=80&w=800&auto=format&fit=crop"
    },
    "Apple FineWoven Wallet with MagSafe": {
        "filename": "apple_magsafe_wallet.jpg",
        "url": "https://images.unsplash.com/photo-1627123424574-724758594e93?q=80&w=800&auto=format&fit=crop"
    },
    "Apple USB-C to Lightning Cable (1m)": {
        "filename": "apple_lightning_cable.jpg",
        "url": "https://images.unsplash.com/photo-1585338107529-13afc5f02586?q=80&w=800&auto=format&fit=crop"
    },
    "Apple USB-C Woven Charge Cable (60W 1m)": {
        "filename": "apple_usbc_woven_cable.jpg",
        "url": "https://images.unsplash.com/photo-1610465299993-e6675c9f9efa?q=80&w=800&auto=format&fit=crop"
    },
    "Apple AirTag (1 Pack)": {
        "filename": "apple_airtag_hd.jpg",
        "url": "https://images.unsplash.com/photo-1623126908029-b8cd78a151b6?q=80&w=800&auto=format&fit=crop"
    },
    "Belkin BoostCharge Pro 3-in-1 MagSafe Charger": {
        "filename": "belkin_3in1_hd.jpg",
        "url": "https://images.unsplash.com/photo-1586953208448-b95a79798f07?q=80&w=800&auto=format&fit=crop"
    },

    # --- OPPO ACCESSORIES ---
    "OPPO SUPERVOOC 80W Power Adapter": {
        "filename": "oppo_80w_charger.jpg",
        "url": "https://images.unsplash.com/photo-1585338107529-13afc5f02586?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Enco Air3 Pro Wireless Earbuds": {
        "filename": "oppo_enco_air3.jpg",
        "url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Enco X2 Noise Cancelling Earbuds": {
        "filename": "oppo_enco_x2.jpg",
        "url": "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Reno11 Pro Magnetic Protective Case": {
        "filename": "oppo_reno11_case.jpg",
        "url": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Find X7 Ultra Premium Leather Case": {
        "filename": "oppo_findx7_leather_case.jpg",
        "url": "https://images.unsplash.com/photo-1601593346740-925612772716?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO 67W SUPERVOOC Car Charger": {
        "filename": "oppo_car_charger_67w.jpg",
        "url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Type-C Fast Charging Cable (8A 1m)": {
        "filename": "oppo_8a_typec_cable.jpg",
        "url": "https://images.unsplash.com/photo-1585338107529-13afc5f02586?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO AirVOOC 50W Wireless Charger Stand": {
        "filename": "oppo_50w_wireless_stand.jpg",
        "url": "https://images.unsplash.com/photo-1622445268465-8478d058864a?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Pad 2 Smart Touch Keyboard Case": {
        "filename": "oppo_pad2_keyboard.jpg",
        "url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?q=80&w=800&auto=format&fit=crop"
    },
    "OPPO Band 2 Fitness Tracker": {
        "filename": "oppo_band_2.jpg",
        "url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?q=80&w=800&auto=format&fit=crop"
    },

    # --- VIVO ACCESSORIES ---
    "Vivo 120W FlashCharge Power Adapter": {
        "filename": "vivo_120w_adapter.jpg",
        "url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo TWS 3 Pro True Wireless Earphones": {
        "filename": "vivo_tws3_pro.jpg",
        "url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo V30 Pro Anti-Drop Armor Case": {
        "filename": "vivo_v30_armor_case.jpg",
        "url": "https://images.unsplash.com/photo-1603313011101-320f26a4f6f6?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo X100 Pro Photography Grip Kit & Case": {
        "filename": "vivo_x100_camera_grip.jpg",
        "url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo 80W FlashCharge Car Charger": {
        "filename": "vivo_80w_car_charger.jpg",
        "url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo 6A Type-C Super Fast Cable (1.2m)": {
        "filename": "vivo_6a_typec_cable.jpg",
        "url": "https://images.unsplash.com/photo-1610465299993-e6675c9f9efa?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo 50W Wireless FlashCharger Stand": {
        "filename": "vivo_50w_wireless_stand.jpg",
        "url": "https://images.unsplash.com/photo-1622445268465-8478d058864a?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo TWS Air2 Lightweight Bluetooth Earbuds": {
        "filename": "vivo_tws_air2.jpg",
        "url": "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo X Fold3 Pro Carbon Fiber Case": {
        "filename": "vivo_xfold3_carbon_case.jpg",
        "url": "https://images.unsplash.com/photo-1601593346740-925612772716?q=80&w=800&auto=format&fit=crop"
    },
    "Vivo Watch 3 Smartwatch (Sport Edition)": {
        "filename": "vivo_watch_3.jpg",
        "url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?q=80&w=800&auto=format&fit=crop"
    },

    # --- HUAWEI ACCESSORIES ---
    "Huawei SuperCharge 88W Max Power Adapter": {
        "filename": "huawei_88w_charger.jpg",
        "url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei FreeBuds Pro 3 ANC Earbuds": {
        "filename": "huawei_freebuds_pro3.jpg",
        "url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei FreeBuds 5i Hi-Res Wireless Earbuds": {
        "filename": "huawei_freebuds_5i.jpg",
        "url": "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei Mate 60 Pro Magnetic Ring Case": {
        "filename": "huawei_mate60_ring_case.jpg",
        "url": "https://images.unsplash.com/photo-1541877944-ac82a091518a?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei Mate X5 Kevlar Protective Cover": {
        "filename": "huawei_matex5_kevlar.jpg",
        "url": "https://images.unsplash.com/photo-1601593346740-925612772716?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei 50W SuperCharge Wireless Car Charger": {
        "filename": "huawei_50w_car_charger.jpg",
        "url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei 6A Type-C SuperCharge Cable (1.5m)": {
        "filename": "huawei_6a_cable.jpg",
        "url": "https://images.unsplash.com/photo-1585338107529-13afc5f02586?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei SuperCharge 50W Vertical Charger Stand": {
        "filename": "huawei_50w_charger_stand.jpg",
        "url": "https://images.unsplash.com/photo-1622445268465-8478d058864a?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei M-Pencil (3rd Gen) NearLink Stylus": {
        "filename": "huawei_mpencil_3rd.jpg",
        "url": "https://images.unsplash.com/photo-1628815858682-192e21b76426?q=80&w=800&auto=format&fit=crop"
    },
    "Huawei Band 9 Fitness Smart Tracker": {
        "filename": "huawei_band_9.jpg",
        "url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?q=80&w=800&auto=format&fit=crop"
    }
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

success_count = 0

for name, item in hd_accessory_images.items():
    file_path = os.path.join(media_products_dir, item["filename"])
    rel_db_path = f"products/{item['filename']}"
    
    try:
        req = urllib.request.Request(item["url"], headers=headers)
        with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
            out_file.write(response.read())
        
        # Update product in Django DB
        updated = Product.objects.filter(name=name).update(image=rel_db_path)
        if updated:
            success_count += 1
            print(f"Downloaded & updated: {name} -> {rel_db_path}")
    except Exception as e:
        print(f"Failed to download for {name}: {e}")

print(f"\nSuccessfully downloaded and set HD web images for {success_count}/40 accessory products!")
