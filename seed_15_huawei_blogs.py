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

HUAWEI_BLOGS = [
    {
        "name": "HUAWEI Mate XT Ultimate",
        "slug": "huawei-mate-xt-ultimate-specifications",
        "filename": "huawei_mate_xt_ultimate_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-mate-xt-ultimate.jpg",
        "description": """📱 អេក្រង់៖ World's First Tri-Foldable LTPO OLED 10.2" (120Hz, 3K Resolution)
🚀 Performance Chip៖ Kirin 9010 (7nm)
🧠 RAM៖ 16GB | Storage: 512GB / 1TB UFS
📷 Camera៖ XMAGE 50MP Variable Aperture (f/1.4-f/4.0, OIS) + 12MP Periscope (5.5x) + 12MP Ultrawide
🔋 Battery៖ 5600 mAh Silicon-Anode, 66W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ ទូរស័ព្ទបត់ ៣ តំបូងគេបង្អស់លើពិភពលោក, ប្តូរទំហំអេក្រង់ 6.4", 7.9" និង 10.2" បែប Tablet"""
    },
    {
        "name": "HUAWEI Pura 70 Ultra",
        "slug": "huawei-pura-70-ultra-specifications",
        "filename": "huawei_pura_70_ultra_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-pura70-ultra.jpg",
        "description": """📱 អេក្រង់៖ 6.8" LTPO OLED (1-120Hz, 2500 nits, Kunlun Glass 2)
🚀 Performance Chip៖ Kirin 9010 (7nm)
🧠 RAM៖ 16GB | Storage: 512GB / 1TB UFS
📷 Camera៖ Retractable 1-inch 50MP Main (f/1.6-f/4.0, Sensor-shift OIS) + 50MP Macro Telephoto (3.5x) + 40MP Ultrawide
🔋 Battery៖ 5200 mAh, 100W SuperCharge + 80W Wireless
🌟 ចំណុចពិសេស៖ កាមេរ៉ាលូតចេញចូល retractable 1-inch ដំបូងគេ, Ultra Speed Snapshot ថតវត្ថុផ្លាស់ទីលឿន 300km/h"""
    },
    {
        "name": "HUAWEI Pura 70 Pro",
        "slug": "huawei-pura-70-pro-specifications",
        "filename": "huawei_pura_70_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-pura70-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.8" LTPO OLED (120Hz, 2500 nits, Kunlun Glass 2)
🚀 Performance Chip៖ Kirin 9010 (7nm)
🧠 RAM៖ 12GB | Storage: 512GB / 1TB UFS
📷 Camera៖ XMAGE 50MP Main (f/1.4-f/4.0, OIS) + 48MP Macro Telephoto (3.5x, 35x Macro) + 12.5MP Ultrawide
🔋 Battery៖ 5050 mAh, 100W SuperCharge + 80W Wireless
🌟 ចំណុចពិសេស៖ ឡែន Macro Telephoto ថតរូបជិត 5cm ច្បាស់លម្អិត, ឌីហ្សាញត្រីកោណ Forward Symbol"""
    },
    {
        "name": "HUAWEI Pura 70",
        "slug": "huawei-pura-70-specifications",
        "filename": "huawei_pura_70_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-pura70.jpg",
        "description": """📱 អេក្រង់៖ 6.6" Flat LTPO OLED (120Hz, Kunlun Glass 2)
🚀 Performance Chip៖ Kirin 9000S1 (7nm)
🧠 RAM៖ 12GB | Storage: 256GB / 512GB / 1TB
📷 Camera៖ XMAGE 50MP Main (f/1.4-f/4.0, OIS) + 12MP Periscope Telephoto (5x Zoom) + 13MP Ultrawide
🔋 Battery៖ 4900 mAh, 66W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ អេក្រង់រស្មីស្មើ Kunlun Glass រឹងមាំ, កាមេរ៉ាមេ Variable Aperture ថតរូបស្អាតគ្រប់លក្ខខណ្ឌ"""
    },
    {
        "name": "HUAWEI Mate 60 Pro",
        "slug": "huawei-mate-60-pro-specifications",
        "filename": "huawei_mate_60_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-mate-60-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.82" LTPO OLED (120Hz, 300Hz Touch Sampling, Second-gen Kunlun Glass)
🚀 Performance Chip៖ Kirin 9000S (7nm)
🧠 RAM៖ 12GB | Storage: 256GB / 512GB / 1TB (គាំទ្រ NM Card 256GB)
📷 Camera៖ 50MP Main (f/1.4-f/4.0, OIS) + 48MP Macro Telephoto (3.5x, OIS) + 12MP Ultrawide
🔋 Battery៖ 5000 mAh, 88W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ សេវាផ្កាយរណប Satellite Calling និយាយទូរស័ព្ទគ្មានសេវា, កញ្ចក់ Kunlun Glass 2 ធន់ខ្លាំង"""
    },
    {
        "name": "HUAWEI Mate 60",
        "slug": "huawei-mate-60-specifications",
        "filename": "huawei_mate_60_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-mate-60.jpg",
        "description": """📱 អេក្រង់៖ 6.69" LTPO OLED (120Hz, Second-gen Kunlun Glass)
🚀 Performance Chip៖ Kirin 9000S (7nm)
🧠 RAM៖ 12GB | Storage: 256GB / 512GB / 1TB
📷 Camera៖ 50MP Main (Variable Aperture OIS) + 12MP Periscope Telephoto (5x) + 12MP Ultrawide
🔋 Battery៖ 4750 mAh, 66W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ Satellite Messaging ផ្ញើសារតាមផ្កាយរណប Beidou, ការពារទឹកកម្រិត IP68"""
    },
    {
        "name": "HUAWEI Mate X5",
        "slug": "huawei-mate-x5-specifications",
        "filename": "huawei_mate_x5_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-mate-x5.jpg",
        "description": """📱 អេក្រង់៖ 7.85" Foldable OLED (120Hz) + 6.4" OLED ក្រៅ (Kunlun Glass)
🚀 Performance Chip៖ Kirin 9000S (7nm)
🧠 RAM៖ 12GB / 16GB | Storage: 512GB / 1TB
📷 Camera៖ XMAGE 50MP Main (OIS) + 12MP Periscope Telephoto (5x, OIS) + 13MP Ultrawide
🔋 Battery៖ 5060 mAh, 66W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ ទូរស័ព្ទបត់រឹងមាំ Xuanwu Tempered Kunlun Glass, ស្តើង 5.3mm ពេលបើក និងការពារទឹក IPX8"""
    },
    {
        "name": "HUAWEI P60 Pro",
        "slug": "huawei-p60-pro-specifications",
        "filename": "huawei_p60_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-p60-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.67" Quad-Curve LTPO OLED (120Hz, Kunlun Glass)
🚀 Performance Chip៖ Qualcomm Snapdragon 8+ Gen 1 4G (4nm)
🧠 RAM៖ 8GB / 12GB | Storage: 256GB / 512GB
📷 Camera៖ Ultra Lighting 48MP Main (f/1.4-f/4.0, OIS) + 48MP Night Vision Telephoto (3.5x, OIS) + 13MP Ultrawide
🔋 Battery៖ 4815 mAh, 88W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ រចនាបថ Rococo Pearl ខ្នងចម្លាក់គុជខ្យងប្លែកពីគេ, កាមេរ៉ា Telephoto ថតរូបយប់ច្បាស់បំផុត"""
    },
    {
        "name": "HUAWEI P60",
        "slug": "huawei-p60-specifications",
        "filename": "huawei_p60_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-p60.jpg",
        "description": """📱 អេក្រង់៖ 6.67" LTPO OLED (120Hz, Kunlun Glass)
🚀 Performance Chip៖ Qualcomm Snapdragon 8+ Gen 1 4G (4nm)
🧠 RAM៖ 8GB | Storage: 128GB / 256GB / 512GB
📷 Camera៖ 48MP Main (Variable Aperture f/1.4-f/4.0, OIS) + 12MP Periscope Telephoto (5x) + 13MP Ultrawide
🔋 Battery៖ 4815 mAh, 66W SuperCharge + 50W Wireless
🌟 ចំណុចពិសេស៖ ប្រព័ន្ធថតរូប XMAGE Camera, អេក្រង់កោងរលូន Kunlun Glass និងថាមពលថ្មធន់"""
    },
    {
        "name": "HUAWEI nova 12 Pro",
        "slug": "huawei-nova-12-pro-specifications",
        "filename": "huawei_nova_12_pro_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-nova-12-pro.jpg",
        "description": """📱 អេក្រង់៖ 6.76" OLED (120Hz, 2160Hz PWM Dimming)
🚀 Performance Chip៖ Kirin 8000 (7nm)
🧠 RAM៖ 12GB | Storage: 256GB / 512GB
📷 Camera៖ 50MP Main (f/1.4-f/4.0 Variable Aperture) + 8MP Ultrawide Macro | Camera មុខ 60MP Dual AF Selfie (2x Zoom)
🔋 Battery៖ 4600 mAh, 100W SuperCharge
🌟 ចំណុចពិសេស៖ កាមេរ៉ាមុខភ្លោះ 60MP Ultra-Wide AF ថត Selfie & Vlog ឥតទប់ជើង, សាក 100W លឿនខ្លាំង"""
    },
    {
        "name": "HUAWEI nova 12s",
        "slug": "huawei-nova-12s-specifications",
        "filename": "huawei_nova_12s_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-nova-12s.jpg",
        "description": """📱 អេក្រង់៖ 6.7" OLED (120Hz, 300Hz Touch Sampling)
🚀 Performance Chip៖ Qualcomm Snapdragon 778G 4G (6nm)
🧠 RAM៖ 8GB | Storage: 256GB
📷 Camera៖ 50MP Ultra Vision Main + 8MP Ultrawide Macro | Camera មុខ 60MP Ultra Wide Portrait
🔋 Battery៖ 4500 mAh, 66W SuperCharge
🌟 ចំណុចពិសេស៖ តួកាយស្តើងត្រឹម 6.88mm, កាមេរ៉ាមុខ 60MP Ultra-wide Angle ថតមនុស្សច្រើនច្បាស់ស្អាត"""
    },
    {
        "name": "HUAWEI nova 11i",
        "slug": "huawei-nova-11i-specifications",
        "filename": "huawei_nova_11i_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-nova-11i.jpg",
        "description": """📱 អេក្រង់៖ 6.8" FullView Display (90Hz, Bezel ស្តើងត្រឹម 1mm)
🚀 Performance Chip៖ Qualcomm Snapdragon 680 4G (6nm)
🧠 RAM៖ 8GB | Storage: 128GB / 256GB
📷 Camera៖ 48MP High-res Main + 2MP Depth | Camera មុខ 16MP
🔋 Battery៖ 5000 mAh, 40W HUAWEI SuperCharge Turbo
🌟 ចំណុចពិសេស៖ អេក្រង់ធំ 6.8 អ៊ីញ គែមស្តើងបំផុត, បំពងសំឡេង 88dB Histen 8.1 Sound និងថ្ម 5000mAh"""
    },
    {
        "name": "HUAWEI nova Y91",
        "slug": "huawei-nova-y91-specifications",
        "filename": "huawei_nova_y91_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-nova-y91.jpg",
        "description": """📱 អេក្រង់៖ 6.95" FHD+ LCD (90Hz Refresh Rate)
🚀 Performance Chip៖ Qualcomm Snapdragon 680 4G (6nm)
🧠 RAM៖ 8GB | Storage: 128GB / 256GB
📷 Camera៖ 50MP AI Dual Camera + 2MP Depth | Camera មុខ 8MP
🔋 Battery៖ 7000 mAh Monster Battery, 22.5W SuperCharge
🌟 ចំណុចពិសេស៖ ថ្មយក្ស 7000 mAh ប្រើបានរហូតដល់ ៣ ថ្ងៃ, អេក្រង់ធំបំផុត 6.95" និងបំពងសំឡេង Dual Stereo"""
    },
    {
        "name": "HUAWEI nova Y71",
        "slug": "huawei-nova-y71-specifications",
        "filename": "huawei_nova_y71_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-nova-y71.jpg",
        "description": """📱 អេក្រង់៖ 6.75" HUAWEI FullView Display (HD+)
🚀 Performance Chip៖ Kirin 710A (14nm)
🧠 RAM៖ 8GB | Storage: 128GB (គាំទ្រ MicroSD 512GB)
📷 Camera៖ 48MP AI Triple Camera + 5MP Ultrawide + 2MP Depth
🔋 Battery៖ 6000 mAh, 22.5W SuperCharge
🌟 ចំណុចពិសេស៖ ថាមពលថ្មធំ 6000 mAh សាក ១ សប្តាហ៍ ២ ដង, អេក្រង់ទូលំទូលាយ 6.75 អ៊ីញ"""
    },
    {
        "name": "HUAWEI Pocket S",
        "slug": "huawei-pocket-s-specifications",
        "filename": "huawei_pocket_s_real.jpg",
        "url": "https://fdn2.gsmarena.com/vv/bigpic/huawei-pocket-s.jpg",
        "description": """📱 អេក្រង់៖ 6.9" Foldable OLED (120Hz) + 1.04" OLED ក្រៅ
🚀 Performance Chip៖ Qualcomm Snapdragon 778G 4G (6nm)
🧠 RAM៖ 8GB | Storage: 128GB / 256GB / 512GB
📷 Camera៖ 40MP RYYB True-Chroma Main + 13MP Ultrawide | Camera មុខ 10.7MP
🔋 Battery៖ 4000 mAh, 40W SuperCharge
🌟 ចំណុចពិសេស៖ ទូរស័ព្ទបត់ទាន់សម័យ Pocket Flip ជាមួយសន្លាក់បត់រឹងមាំ និងសែនស័រ RYYB ថតរូបពន្លឺទាប"""
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
    print(f"Starting seed process and image download for {len(HUAWEI_BLOGS)} Huawei models...")
    count = 0
    for idx, item in enumerate(HUAWEI_BLOGS, 1):
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
