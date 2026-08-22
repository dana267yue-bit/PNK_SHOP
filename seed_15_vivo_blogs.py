import os
import sys
import urllib.request
import django
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

try:
    django.setup()
except Exception as e:
    print(f"Setup error: {e}")
    sys.exit(1)

from shop.models import Blog

MEDIA_BLOGS_DIR = os.path.join('media', 'blogs')
os.makedirs(MEDIA_BLOGS_DIR, exist_ok=True)

VIVO_BLOGS = [
    {
        "name": "vivo X Fold3 Pro",
        "slug": "vivo-x-fold3-pro-specifications",
        "filename": "vivo_x_fold3_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x-fold3-pro.jpg",
        "description": """📱 អេក្រង់៖ 8.03" Foldable LTPO AMOLED (120Hz, 4500 nits) + 6.53" AMOLED ក្រៅ
🚀 Performance Chip៖ Qualcomm Snapdragon 8 Gen 3 (4nm)
🧠 RAM៖ 16GB LPDDR5X | Storage: 512GB / 1TB UFS 4.0
📷 Camera៖ ZEISS Optics 50MP Main (OIS) + 64MP Periscope Telephoto (3x Zoom) + 50MP Ultrawide
🔋 Battery៖ 5700 mAh, 100W FlashCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ ទូរស័ព្ទបត់ស្តើងស្រាលបំផុត ជាមួយឡែន ZEISS, ថ្ម Silicon-Carbon 5700mAh និងការពារទឹក IPX8"""
    },
    {
        "name": "vivo X100 Pro",
        "slug": "vivo-x100-pro-specifications",
        "filename": "vivo_x100_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.78" LTPO AMOLED (120Hz, 3000 nits Peak Brightness)
🚀 Performance Chip៖ MediaTek Dimensity 9300 (4nm) + vivo V3 Imaging Chip
🧠 RAM៖ 12GB / 16GB | Storage: 256GB / 512GB / 1TB UFS 4.0
📷 Camera៖ ZEISS 1-inch 50MP Sony IMX989 + 50MP APO Periscope Telephoto (4.3x) + 50MP Ultrawide
🔋 Battery៖ 5400 mAh, 100W FlashCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ កាមេរ៉ា ZEISS APO Telephoto កម្រិតអាជីព, ឈីប Dimensity 9300 កម្លាំងខ្លាំង និងការពារទឹក IP68"""
    },
    {
        "name": "vivo X100",
        "slug": "vivo-x100-specifications",
        "filename": "vivo_x100_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x100.jpg",
        "description": """📱 អេក្រង់៖ 6.78" LTPO AMOLED (120Hz, 3000 nits)
🚀 Performance Chip៖ MediaTek Dimensity 9300 (4nm)
🧠 RAM៖ 12GB / 16GB | Storage: 256GB / 512GB UFS 4.0
📷 Camera៖ ZEISS 50MP Main (VCS True Color) + 64MP Telephoto (3x Zoom, OIS) + 50MP Ultrawide
🔋 Battery៖ 5000 mAh, 120W Dual-Cell FlashCharge
🌟 ចំណុចពិសេស៖ រចនាបថ Sun Ring Design, កាមេរ៉ា ZEISS ថតរូបពណ៌ធម្មជាតិ និងសាក 120W លឿនខ្លាំង"""
    },
    {
        "name": "vivo X90 Pro",
        "slug": "vivo-x90-pro-specifications",
        "filename": "vivo_x90_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-x90-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.78" Curved AMOLED (120Hz, 1300 nits)
🚀 Performance Chip៖ MediaTek Dimensity 9200 (4nm) + vivo V2 NPU
🧠 RAM៖ 12GB LPDDR5X | Storage: 256GB / 512GB UFS 4.0
📷 Camera៖ ZEISS 1-inch 50.3MP Sony IMX989 (OIS) + 50MP Portrait (2x) + 12MP Ultrawide
🔋 Battery៖ 4870 mAh, 120W FlashCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ សែនស័រ 1 អ៊ីញ ថតយប់ច្បាស់ឥតខ្ចោះ ជាមួយ ZEISS T* Coating និងខ្នងស្បែកសេរ៉ាមិច"""
    },
    {
        "name": "vivo V30 Pro 5G",
        "slug": "vivo-v30-pro-5g-specifications",
        "filename": "vivo_v30_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.78" 3D Curved AMOLED 1.5K (120Hz, 2800 nits)
🚀 Performance Chip៖ MediaTek Dimensity 8200 (4nm)
🧠 RAM៖ 12GB (+12GB Extended RAM) | Storage: 512GB UFS 3.1
📷 Camera៖ ZEISS Triple Main 50MP Sony IMX920 + 50MP Telephoto Portrait + 50MP Ultrawide + Aura Light Portrait
🔋 Battery៖ 5000 mAh, 80W FlashCharge
🌟 ចំណុចពិសេស៖ V-Series ដំបូងគេដែលមានឡែន ZEISS, Aura Light Portrait ជំនាន់ថ្មី និងរចនាបថស្តើងបំផុត"""
    },
    {
        "name": "vivo V30 5G",
        "slug": "vivo-v30-5g-specifications",
        "filename": "vivo_v30_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-lite.jpg",
        "description": """📱 អេក្រង់៖ 6.78" 3D Curved AMOLED 1.5K (120Hz, 2800 nits)
🚀 Performance Chip៖ Qualcomm Snapdragon 7 Gen 3 (4nm)
🧠 RAM៖ 12GB | Storage: 256GB / 512GB
📷 Camera៖ 50MP VCS True Color Main (OIS) + 50MP Ultrawide | Camera មុខ 50MP Group Selfie (AF)
🔋 Battery៖ 5000 mAh, 80W FlashCharge
🌟 ចំណុចពិសេស៖ ភ្លើង Aura Light Portrait ធំជាងមុន 19 ដង, ឌីហ្សាញផ្ការីក 3D Petal Pattern ស្អាតប្លែក"""
    },
    {
        "name": "vivo V29 Pro 5G",
        "slug": "vivo-v29-pro-5g-specifications",
        "filename": "vivo_v29_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v29-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.78" 3D Curved AMOLED (120Hz, HDR10+)
🚀 Performance Chip៖ MediaTek Dimensity 8200 (4nm)
🧠 RAM៖ 12GB | Storage: 256GB UFS 3.1
📷 Camera៖ 50MP Sony IMX766V (OIS) + 12MP Portrait (2x) + 8MP Ultrawide + Smart Aura Light
🔋 Battery៖ 4600 mAh, 80W FlashCharge (សាក 18 នាទីបាន 50%)
🌟 ចំណុចពិសេស៖ Smart Aura Light កែតម្រូវសីតុណ្ហភាពពន្លឺស្វ័យប្រវត្តិ, កាមេរ៉ា Portrait ថតរូបស្បែកស្អាត"""
    },
    {
        "name": "vivo V29e 5G",
        "slug": "vivo-v29e-5g-specifications",
        "filename": "vivo_v29e_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v29e.jpg",
        "description": """📱 អេក្រង់៖ 6.67" Flat AMOLED (120Hz, 1150 nits)
🚀 Performance Chip៖ Qualcomm Snapdragon 695 5G (6nm)
🧠 RAM៖ 8GB / 12GB | Storage: 256GB
📷 Camera៖ 64MP OIS Night Camera + 8MP Ultrawide | Camera មុខ 50MP Eye AF Selfie
🔋 Battery៖ 4800 mAh, 44W FlashCharge
🌟 ចំណុចពិសេស៖ កាមេរ៉ាមុខ 50MP Autofocus ថតរូប Selfie ច្បាស់បំផុត, ឌីហ្សាញតួកាយស្តើងស្រាល"""
    },
    {
        "name": "vivo V27 5G",
        "slug": "vivo-v27-5g-specifications",
        "filename": "vivo_v27_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-v27.jpg",
        "description": """📱 អេក្រង់៖ 6.78" 3D Curved AMOLED (120Hz)
🚀 Performance Chip៖ MediaTek Dimensity 7200 (4nm)
🧠 RAM៖ 8GB / 12GB | Storage: 256GB
📷 Camera៖ 50MP Sony IMX766V (OIS) + 8MP Ultrawide + 2MP Macro + Aura Light
🔋 Battery៖ 4600 mAh, 66W FlashCharge
🌟 ចំណុចពិសេស៖ ខ្នងកញ្ចក់ប្តូរពណ៌ពេលត្រូវពន្លឺព្រះអាទិត្យ (Color Changing Fluorite AG Glass)"""
    },
    {
        "name": "vivo Y200e 5G",
        "slug": "vivo-y200e-5g-specifications",
        "filename": "vivo_y200e_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y200e-5g.jpg",
        "description": """📱 អេក្រង់៖ 6.67" AMOLED (120Hz, 1200 nits)
🚀 Performance Chip៖ Qualcomm Snapdragon 4 Gen 2 (4nm)
🧠 RAM៖ 6GB / 8GB | Storage: 128GB
📷 Camera៖ 50MP Main + 2MP Flicker Sensor | Camera មុខ 16MP
🔋 Battery៖ 5000 mAh, 44W FlashCharge
🌟 ចំណុចពិសេស៖ ខ្នងស្បែក Eco-Fiber Leather ដំបូងគេលើត្រកូល Y Series, លំអៀងសំឡេង 300% Dual Stereo Speakers"""
    },
    {
        "name": "vivo Y100 5G",
        "slug": "vivo-y100-5g-specifications",
        "filename": "vivo_y100_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y100-5g-indonesia.jpg",
        "description": """📱 អេក្រង់៖ 6.67" Ultra Vision AMOLED (120Hz, 1200 nits)
🚀 Performance Chip៖ Qualcomm Snapdragon 4 Gen 2 (4nm)
🧠 RAM៖ 8GB (+8GB Extended RAM) | Storage: 128GB / 256GB
📷 Camera៖ 50MP Main Camera + 8MP Ultrawide + Flicker Sensor
🔋 Battery៖ 5000 mAh, 80W FlashCharge (សាក 30 នាទីបាន 80%)
🌟 ចំណុចពិសេស៖ សាកលឿន 80W លើទូរស័ព្ទតម្លៃសមរម្យ, ឌីហ្សាញស្បែក Purple Leather & ធន់ IP54"""
    },
    {
        "name": "vivo Y36 5G",
        "slug": "vivo-y36-5g-specifications",
        "filename": "vivo_y36_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y36-5g.jpg",
        "description": """📱 អេក្រង់៖ 6.64" FHD+ Dotch Display (90Hz, 650 nits)
🚀 Performance Chip៖ MediaTek Dimensity 6020 (7nm)
🧠 RAM៖ 8GB | Storage: 256GB (គាំទ្រ MicroSD 1TB)
📷 Camera៖ 50MP HD Main + 2MP Bokeh | Camera មុខ 16MP
🔋 Battery៖ 5000 mAh, 44W FlashCharge
🌟 ចំណុចពិសេស៖ ឌីហ្សាញកញ្ចក់ Fantasy Frame, អេក្រង់ធំភ្លឺច្បាស់ និងធន់នឹងការការពារទឹកជម្រាត IP54"""
    },
    {
        "name": "vivo Y27 5G",
        "slug": "vivo-y27-5g-specifications",
        "filename": "vivo_y27_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y27-5g.jpg",
        "description": """📱 អេក្រង់៖ 6.64" FHD+ Sunlight Display (600 nits)
🚀 Performance Chip៖ MediaTek Dimensity 6020 (7nm)
🧠 RAM៖ 6GB / 8GB | Storage: 128GB
📷 Camera៖ 50MP Ultra Clear Main + 2MP Bokeh
🔋 Battery៖ 5000 mAh, 44W FlashCharge
🌟 ចំណុចពិសេស៖ ឌីហ្សាញ Dual-Ring Design, ថ្ម 5000mAh ប្រើបានពេញមួយថ្ងៃ និងសាក 44W លឿន"""
    },
    {
        "name": "vivo Y17s",
        "slug": "vivo-y17s-specifications",
        "filename": "vivo_y17s_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y17s.jpg",
        "description": """📱 អេក្រង់៖ 6.56" HD+ High Brightness Display (840 nits)
🚀 Performance Chip៖ MediaTek Helio G85 (12nm)
🧠 RAM៖ 4GB / 6GB | Storage: 128GB
📷 Camera៖ 50MP Corporate Camera + 2MP Depth | Camera មុខ 8MP
🔋 Battery៖ 5000 mAh, 15W Fast Charge
🌟 ចំណុចពិសេស៖ អេក្រង់ភ្លឺច្បាស់ 840 nits ប្រើក្រៅផ្ទះងាយស្រួល, ការពារទឹក IP54 និងតម្លៃធូរថ្លៃ"""
    },
    {
        "name": "vivo Y03",
        "slug": "vivo-y03-specifications",
        "filename": "vivo_y03_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/vivo-y03.jpg",
        "description": """📱 អេក្រង់៖ 6.56" HD+ Sunlight Display (90Hz)
🚀 Performance Chip៖ MediaTek Helio G85 (12nm)
🧠 RAM៖ 4GB | Storage: 64GB / 128GB
📷 Camera៖ 13MP Main + QVGA Lens | Camera មុខ 5MP
🔋 Battery៖ 5000 mAh, 15W Fast Charge
🌟 ចំណុចពិសេស៖ អេក្រង់ 90Hz រលូន, ថ្មធំ 5000mAh និងតួកាយការពារជម្រកទឹក IP54 ធន់មាំ"""
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def make_clean_card(src_path, dst_path):
    try:
        orig = Image.open(src_path).convert("RGBA")
        W, H = 600, 420
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        
        o_w, o_h = orig.size
        ratio = min((W - 60) / o_w, (H - 40) / o_h)
        new_w = int(o_w * ratio)
        new_h = int(o_h * ratio)
        
        resized = orig.resize((new_w, new_h), Image.Resampling.LANCZOS)
        pos_x = (W - new_w) // 2
        pos_y = (H - new_h) // 2
        
        canvas.paste(resized, (pos_x, pos_y), resized)
        final_rgb = canvas.convert("RGB")
        final_rgb.save(dst_path, "JPEG", quality=98)
        return True
    except Exception as e:
        print(f"Error processing image {src_path}: {e}")
        return False

def run():
    print(f"Starting seed process and image download for {len(VIVO_BLOGS)} Vivo models...")
    count = 0
    for idx, item in enumerate(VIVO_BLOGS, 1):
        raw_path = os.path.join(MEDIA_BLOGS_DIR, f"raw_{item['filename']}")
        card_path = os.path.join(MEDIA_BLOGS_DIR, item['filename'])
        
        try:
            req = urllib.request.Request(item["url"], headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp, open(raw_path, 'wb') as f:
                f.write(resp.read())
            make_clean_card(raw_path, card_path)
        except Exception as e:
            print(f"Download failed for {item['name']}: {e}")
            
        db_image_path = f"blogs/{item['filename']}"
        blog_obj, created = Blog.objects.update_or_create(
            slug=item["slug"],
            defaults={
                "name": item["name"],
                "description": item["description"],
                "image": db_image_path
            }
        )
        action = "Created" if created else "Updated"
        print(f"[{idx}/15] {action} Blog ID {blog_obj.id}: {blog_obj.name}")
        count += 1
        
    print(f"\nCOMPLETED! Total blogs in database: {Blog.objects.count()}")

if __name__ == '__main__':
    run()
