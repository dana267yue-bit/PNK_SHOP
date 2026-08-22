import os
import sys
import shutil
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNK.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    django.setup()
except Exception as e:
    print(f"Setup error: {e}")
    sys.exit(1)

from shop.models import Blog
from PIL import Image, ImageDraw, ImageFont

MEDIA_BLOGS_DIR = os.path.join('media', 'blogs')
os.makedirs(MEDIA_BLOGS_DIR, exist_ok=True)

# Helper to create/ensure image cover exists
def ensure_image(filename, title_text, bg_color, accent_color=(0, 210, 150)):
    target_path = os.path.join(MEDIA_BLOGS_DIR, filename)
    if os.path.exists(target_path):
        return f"blogs/{filename}"

    # Generate stylish banner image using PIL
    img = Image.new('RGB', (800, 500), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Draw modern geometric design & borders
    draw.rectangle([15, 15, 785, 485], outline=accent_color, width=3)
    draw.line([(30, 80), (770, 80)], fill=accent_color, width=2)
    draw.line([(30, 420), (770, 420)], fill=accent_color, width=2)

    # Brand badge
    draw.rectangle([300, 35, 500, 70], fill=accent_color)
    draw.text((400, 52), "OPPO FLAGSHIP", fill=(255, 255, 255), anchor="mm")

    # Main title & Subtitle
    draw.text((400, 220), title_text, fill=(255, 255, 255), anchor="mm", align="center")
    draw.text((400, 290), "Specifications & Key Features", fill=(200, 240, 225), anchor="mm", align="center")
    draw.text((400, 450), "PNK PHONE SHOP OFFICIAL BLOG", fill=(180, 180, 180), anchor="mm", align="center")

    img.save(target_path)
    return f"blogs/{filename}"

OPPO_BLOG_DATA = [
    {
        "name": "OPPO Find N3",
        "slug": "oppo-find-n3-specifications",
        "image_file": "oppo-find-n3_cover.png",
        "bg_color": (15, 42, 35),
        "accent_color": (0, 204, 136),
        "title_badge": "OPPO Find N3 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Find N3៖

📱 ទំហំអេក្រង់៖ 7.82" Foldable LTPO3 OLED (120Hz, 2800 nits Peak) + អេក្រង់ក្រៅ 6.31" LTPO3 OLED (120Hz)
📺 Resolution៖ 2268 x 2440 ភីកសែល (អេក្រង់ក្នុង) | 1116 x 2484 ភីកសែល (អេក្រង់ក្រៅ)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ក្របខ័ណ្ឌ Stainless Steel & Titanium | ជម្រើសពណ៌៖ Black (Leather), Gold, Green
🚀 Performance Chip៖ Qualcomm Snapdragon 8 Gen 2 (4nm)
⚡ CPU៖ Octa-core (1x3.2 GHz Cortex-X3 + 2x2.8 GHz Cortex-A715 + 2x2.8 GHz Cortex-A710 + 3x2.0 GHz Cortex-A510)
🧠 RAM៖ 16GB LPDDR5X
💾 Storage (ទំហំផ្ទុក)៖ 512GB / 1TB UFS 4.0

🌟 ចំណុចពិសេស៖
- ទូរស័ព្ទបត់កម្រិត Flagship ជាមួយកាមេរ៉ា Hasselblad Foldable Camera System
- កាមេរ៉ា 3 គ្រាប់៖ 48MP Wide (Sony LYT-T808) + 64MP Periscope Telephoto (3x Zoom, OIS) + 48MP Ultrawide
- អេក្រង់ភ្លឺច្បាស់រហូតដល់ 2800 nits និងគ្មានស្នាមបត់ (Crease-free display)
- ថាមពលថ្ម 4805 mAh គាំទ្រសាកលឿន 67W SUPERVOOC
- មុខងាររៀបចំអេក្រង់ដោះស្រាយការងារ Multitasking (Boundless View)"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Find N3 Flip",
        "slug": "oppo-find-n3-flip-specifications",
        "image_file": "oppo-find-n3-flip_cover.png",
        "bg_color": (28, 36, 48),
        "accent_color": (230, 160, 200),
        "title_badge": "OPPO Find N3 Flip",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Find N3 Flip៖

📱 ទំហំអេក្រង់៖ 6.8" Foldable LTPO AMOLED (120Hz) + អេក្រង់ក្រៅទម្រង់បញ្ឈរ 3.26" SD AMOLED
📺 Resolution៖ 1080 x 2520 ភីកសែល (អេក្រង់ក្នុង) | 382 x 720 ភីកសែល (អេក្រង់ក្រៅ)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ កញ្ចក់ Gorilla Glass Victus ខាងក្រៅ, ក្របខ័ណ្ឌ អាលុយមីញ៉ូម | ជម្រើសពណ៌៖ Astral Black, Moonlit Gold, Sleek Rose
🚀 Performance Chip៖ MediaTek Dimensity 9200 (4nm)
⚡ CPU៖ Octa-core (1x3.05 GHz Cortex-X3 + 3x2.85 GHz Cortex-A715 + 4x1.80 GHz Cortex-A510)
🧠 RAM៖ 12GB LPDDR5X
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB UFS 4.0

🌟 ចំណុចពិសេស៖
- Flip Phone ដំបូងគេដែលមានប្រព័ន្ធកាមេរ៉ា 3 គ្រាប់ Hasselblad
- កាមេរ៉ា 3 គ្រាប់៖ 50MP Main (OIS) + 32MP Telephoto Portrait (2x) + 48MP Ultrawide
- អេក្រង់ក្រៅទម្រង់បញ្ឈរ 3.26 អ៊ីញ ដំណើរការ Mini Apps បានយ៉ាងច្រើន
- Alert Slider ប្តូរកម្រិតសំឡេងរហ័ស លើតួកាយបត់
- ថាមពលថ្ម 4300 mAh និងសាកលឿន 44W SUPERVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Find X8 Pro",
        "slug": "oppo-find-x8-pro-specifications",
        "image_file": "oppo-find-x8-pro_cover.png",
        "bg_color": (20, 30, 45),
        "accent_color": (0, 180, 210),
        "title_badge": "OPPO Find X8 Pro",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Find X8 Pro៖

📱 ទំហំអេក្រង់៖ 6.78" LTPO AMOLED (120Hz, Dolby Vision, 4500 nits Peak Brightness)
📺 Resolution៖ 1264 x 2780 ភីកសែល (~450 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ កញ្ចក់ Gorilla Glass Victus 2, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Starfield Black, Pearl White, Space Blue
🚀 Performance Chip៖ MediaTek Dimensity 9400 (3nm)
⚡ CPU៖ Octa-core (1x3.63 GHz Cortex-X925 + 3x3.3 GHz Cortex-X4 + 4x2.4 GHz Cortex-A720)
🧠 RAM៖ 12GB / 16GB
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB / 1TB UFS 4.0

🌟 ចំណុចពិសេស៖
- ប្រព័ន្ធកាមេរ៉ា Hasselblad 4 គ្រាប់ Telephoto ២ គ្រាប់៖ 50MP Main + 50MP Ultrawide + 50MP Periscope (3x) + 50MP Periscope (6x)
- ប៊ូតុង Quick Button សម្រាប់បញ្ជាកាមេរ៉ា ថតរូប និង Zoom យ៉ាងរហ័ស
- ថាមពលថ្ម Silicon-Carbon 5910 mAh សាកលឿន 80W Wired + 50W Wireless AIRVOOC
- ឈីប MediaTek Dimensity 9400 3nm លឿនរហ័សបំផុត និងសន្សំសំចៃថាមពល
- ការពារទឹក និងធូលីកម្រិត IP68 / IP69"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Find X7 Ultra",
        "slug": "oppo-find-x7-ultra-specifications",
        "image_file": "oppo-find-x7-ultra_cover.png",
        "bg_color": (40, 30, 25),
        "accent_color": (220, 150, 80),
        "title_badge": "OPPO Find X7 Ultra",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Find X7 Ultra៖

📱 ទំហំអេក្រង់៖ 6.82" LTPO AMOLED 2K (120Hz, Dolby Vision, 4500 nits)
📺 Resolution៖ 1440 x 3168 ភីកសែល (~510 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ខ្នងស្បែក Premium Leather & Glass | ជម្រើសពណ៌៖ Ocean Blue, Sepia Brown, Tailored Black
🚀 Performance Chip៖ Qualcomm Snapdragon 8 Gen 3 (4nm)
⚡ CPU៖ Octa-core (1x3.3 GHz Cortex-X4 + 3x3.15 GHz Cortex-A720 + 2x2.96 GHz Cortex-A720 + 2x2.27 GHz Cortex-A520)
🧠 RAM៖ 12GB / 16GB LPDDR5X
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB UFS 4.0

🌟 ចំណុចពិសេស៖
- World's First Dual Periscope Camera System៖ 50MP Sony LYT-900 1-inch + 50MP Ultrawide + 50MP Periscope 3x + 50MP Periscope 6x
- ប្រព័ន្ធកែសម្រួលពណ៌រូបថតពី Hasselblad HyperTone Image Engine
- អេក្រង់ 2K OLED ភ្លឺច្បាស់បំពង់កំពូល 4500 nits
- ថាមពលថ្ម 5000 mAh គាំទ្រសាកលឿន 100W SUPERVOOC និង 50W Wireless
- VIP Mode សម្រាប់ការពារឯកជនភាព hardware privacy switch"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Find X7",
        "slug": "oppo-find-x7-specifications",
        "image_file": "oppo-find-x7_cover.png",
        "bg_color": (32, 24, 45),
        "accent_color": (160, 100, 240),
        "title_badge": "OPPO Find X7",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Find X7៖

📱 ទំហំអេក្រង់៖ 6.78" LTPO AMOLED (120Hz, 4500 nits Peak Brightness)
📺 Resolution៖ 1264 x 2780 ភីកសែល (~450 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ កញ្ចក់ & ស្បែក Premium Leather | ជម្រើសពណ៌៖ Ocean Blue, Desert Silver, Smokey Purple, Starry Black
🚀 Performance Chip៖ MediaTek Dimensity 9300 (4nm)
⚡ CPU៖ Octa-core (1x3.25 GHz Cortex-X4 + 3x2.85 GHz Cortex-X4 + 4x2.0 GHz Cortex-A720)
🧠 RAM៖ 12GB / 16GB
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB / 1TB UFS 4.0

🌟 ចំណុចពិសេស៖
- ប្រព័ន្ធកាមេរ៉ា 3 គ្រាប់ Hasselblad៖ 50MP Main (Sony Large Sensor) + 50MP Ultrawide + 64MP Periscope Telephoto (3x Zoom, OIS)
- ឈីប Dimensity 9300 All-Big-Core CPU ដំណើរការលឿនខ្លាំង
- ថាមពលថ្ម 5000 mAh សាកលឿន 100W SUPERVOOC
- ប្រព័ន្ធត្រជាក់ Vapor Chamber ធំ ទប់ស្កាត់កម្ដៅពេលលេងហ្គេម"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Find X6 Pro",
        "slug": "oppo-find-x6-pro-specifications",
        "image_file": "oppo-find-x6-pro_cover.png",
        "bg_color": (38, 32, 28),
        "accent_color": (210, 140, 60),
        "title_badge": "OPPO Find X6 Pro",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Find X6 Pro៖

📱 ទំហំអេក្រង់៖ 6.82" LTPO3 AMOLED 2K (120Hz, 2500 nits Peak)
📺 Resolution៖ 1440 x 3168 ភីកសែល (~510 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ក្របខ័ណ្ឌ អាលុយមីញ៉ូម, ខ្នងស្បែកពីរពណ៌ | ជម្រើសពណ៌៖ Brown (Leather), Green, Black
🚀 Performance Chip៖ Qualcomm Snapdragon 8 Gen 2 (4nm)
⚡ CPU៖ Octa-core (1x3.2 GHz Cortex-X3 + 2x2.8 GHz Cortex-A715 + 2x2.8 GHz Cortex-A710 + 3x2.0 GHz Cortex-A510)
🧠 RAM៖ 12GB / 16GB LPDDR5X
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB UFS 4.0

🌟 ចំណុចពិសេស៖
- Three Main Sensors Camera System៖ កាមេរ៉ា 3 គ្រាប់សុទ្ធតែជាសែនស័រធំ 50MP (1-inch Sony IMX989 Main + 50MP Ultrawide + 50MP Periscope Telephoto)
- MariSilicon X Imaging NPU ជំនួយការថតរូប និងវីដេអូពេលយប់ 4K Night Video
- Hasselblad Natural Color Calibration ផ្តល់ពណ៌រូបថតធម្មជាតិច្បាស់
- ថាមពលថ្ម 5000 mAh, 100W SUPERVOOC + 50W Wireless AIRVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Reno 12 Pro 5G",
        "slug": "oppo-reno-12-pro-5g-specifications",
        "image_file": "oppo-reno-12-pro-5g_cover.png",
        "bg_color": (22, 38, 50),
        "accent_color": (80, 180, 250),
        "title_badge": "OPPO Reno 12 Pro 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Reno 12 Pro 5G៖

📱 ទំហំអេក្រង់៖ 6.7" Quad-Curved AMOLED (120Hz, HDR10+, Corning Gorilla Glass Victus 2)
📺 Resolution៖ 1080 x 2412 ភីកសែល (~394 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ក្របខ័ណ្ឌ អាលុយមីញ៉ូម, គែមបត់ Quad-curved | ជម្រើសពណ៌៖ Nebula Silver, Space Brown
🚀 Performance Chip៖ MediaTek Dimensity 7300-Energy (4nm)
⚡ CPU៖ Octa-core (4x2.5 GHz Cortex-A78 + 4x2.0 GHz Cortex-A55)
🧠 RAM៖ 12GB (+12GB Virtual RAM)
💾 Storage (ទំហំផ្ទុក)៖ 512GB UFS 3.1 (គាំទ្រ MicroSD រហូតដល់ 1TB)

🌟 ចំណុចពិសេស៖
- ប្រព័ន្ធ AI Phone៖ AI Eraser 2.0 (លុបរូបភាពមិនလိုចង់), AI Studio, AI Clear Face & AI LinkBoost
- កាមេរ៉ា៖ 50MP Sony LYT-600 (OIS) + 50MP Telephoto Portrait (2x) + 8MP Ultrawide | Camera មុខ 50MP AF
- តួកាយរឹងមាំ All-Round Armor Structure ធន់នឹងការធ្លាក់ និងការពារទឹក IP65
- ថាមពលថ្ម 5000 mAh គាំទ្រសាកលឿន 80W SUPERVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Reno 12 5G",
        "slug": "oppo-reno-12-5g-specifications",
        "image_file": "oppo-reno-12-5g_cover.png",
        "bg_color": (18, 45, 42),
        "accent_color": (40, 210, 170),
        "title_badge": "OPPO Reno 12 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Reno 12 5G៖

📱 ទំហំអេក្រង់៖ 6.7" 3D Curved AMOLED (120Hz, HDR10+, Gorilla Glass 7i)
📺 Resolution៖ 1080 x 2412 ភីកសែល (~394 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ រចនាបថ Fluid Wave 3D | ជម្រើសពណ៌៖ Astro Silver, Sunset Peach, Matte Brown
🚀 Performance Chip៖ MediaTek Dimensity 7300-Energy (4nm)
⚡ CPU៖ Octa-core (4x2.5 GHz Cortex-A78 + 4x2.0 GHz Cortex-A55)
🧠 RAM៖ 12GB
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB UFS 3.1

🌟 ចំណុចពិសេស៖
- មុខងារ AI Features៖ AI Eraser 2.0, AI Summary, AI Speak & AI LinkBoost
- សេវា BeaconLink អាចខលប្រព័ន្ធប៊្លូធូសចម្ងាយជិត ដោយមិនចាំបាច់មានសេវាទូរស័ព្ទ
- កាមេរ៉ា៖ 50MP Sony LYT-600 (OIS) + 8MP Ultrawide + 2MP Macro | Camera មុខ 32MP
- ថាមពលថ្ម 5000 mAh, 80W SUPERVOOC Fast Charge សាក 46 នាទីពេញ"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Reno 11 Pro 5G",
        "slug": "oppo-reno-11-pro-5g-specifications",
        "image_file": "oppo-reno-11-pro-5g_cover.png",
        "bg_color": (35, 25, 40),
        "accent_color": (190, 120, 230),
        "title_badge": "OPPO Reno 11 Pro 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Reno 11 Pro 5G៖

📱 ទំហំអេក្រង់៖ 6.7" 3D Curved OLED (120Hz, HDR10+)
📺 Resolution៖ 1080 x 2412 ភីកសែល (~394 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ រចនាបថ Natural Gemstone Design | ជម្រើសពណ៌៖ Pearl White, Rock Grey
🚀 Performance Chip៖ MediaTek Dimensity 8200 (4nm)
⚡ CPU៖ Octa-core (1x3.1 GHz Cortex-A78 + 3x3.0 GHz Cortex-A78 + 4x2.0 GHz Cortex-A55)
🧠 RAM៖ 12GB
💾 Storage (ទំហំផ្ទុក)៖ 512GB UFS 3.1

🌟 ចំណុចពិសេស៖
- ជំនាញថតរូប Portrait៖ 32MP Sony IMX709 Telephoto Portrait Camera (2x Optical Zoom)
- កាមេរ៉ាមេ 50MP Sony IMX890 ជាមួយ OIS + 8MP Ultrawide
- ឈីប Dimensity 8200 ល្បឿនលឿន និងទប់កម្ដៅបានល្អ
- ថាមពលថ្ម 4600 mAh ជាមួយបច្ចេកវិទ្យាសាកលឿន 80W SUPERVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Reno 11 5G",
        "slug": "oppo-reno-11-5g-specifications",
        "image_file": "oppo-reno-11-5g_cover.png",
        "bg_color": (16, 40, 48),
        "accent_color": (0, 190, 200),
        "title_badge": "OPPO Reno 11 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Reno 11 5G៖

📱 ទំហំអេក្រង់៖ 6.7" 3D Curved OLED (120Hz, HDR10+)
📺 Resolution៖ 1080 x 2412 ភីកសែល (~394 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ឌីហ្សាញបែបលំនាំរលកសមុទ្រ | ជម្រើសពណ៌៖ Wave Green, Rock Grey
🚀 Performance Chip៖ MediaTek Dimensity 7050 (6nm)
⚡ CPU៖ Octa-core (2x2.6 GHz Cortex-A78 + 6x2.0 GHz Cortex-A55)
🧠 RAM៖ 12GB
💾 Storage (ទំហំផ្ទុក)៖ 256GB UFS 2.2

🌟 ចំណុចពិសេស៖
- កាមេរ៉ា 32MP Telephoto Portrait Expert Specialist ថតរូបព្រិលខ្នងធម្មជាតិ
- កាមេរ៉ាមេ 50MP Sony LYT-600 (OIS) + 8MP Ultrawide
- ថាមពលថ្មធំ 5000 mAh គាំទ្រសាកលឿន 67W SUPERVOOC
- ប្រព័ន្ធប្រតិបត្តិការ ColorOS 14 រលូន និងមានសុវត្ថិភាព"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO Reno 10 Pro+ 5G",
        "slug": "oppo-reno-10-pro-plus-5g-specifications",
        "image_file": "oppo-reno-10-pro-plus-5g_cover.png",
        "bg_color": (40, 20, 30),
        "accent_color": (230, 90, 140),
        "title_badge": "OPPO Reno 10 Pro+ 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO Reno 10 Pro+ 5G៖

📱 ទំហំអេក្រង់៖ 6.74" 3D Curved OLED 1.5K (120Hz, HDR10+, 1400 nits)
📺 Resolution៖ 1240 x 2772 ភីកសែល (~450 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ក្របខ័ណ្ឌ អាលុយមីញ៉ូម | ជម្រើសពណ៌៖ Silvery Grey, Glossy Purple
🚀 Performance Chip៖ Qualcomm Snapdragon 8+ Gen 1 (4nm)
⚡ CPU៖ Octa-core (1x3.0 GHz Cortex-X2 + 3x2.5 GHz Cortex-A710 + 4x1.80 GHz Cortex-A510)
🧠 RAM៖ 12GB / 16GB LPDDR5
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB UFS 3.1

🌟 ចំណុចពិសេស៖
- កាមេរ៉ា Periscope Telephoto 64MP (3x Optical Zoom, OIS) លើ Reno Series ដំបូងគេ
- កាមេរ៉ាមេ 50MP Sony IMX890 (OIS) + 8MP Ultrawide
- ឈីប Snapdragon 8+ Gen 1 កម្លាំងខ្លាំងក្លាសម្រាប់ gaming
- ថាមពលថ្ម 4700 mAh និងសាកលឿនបំផុត 100W SUPERVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO A3 Pro 5G",
        "slug": "oppo-a3-pro-5g-specifications",
        "image_file": "oppo-a3-pro-5g_cover.png",
        "bg_color": (20, 35, 30),
        "accent_color": (60, 200, 120),
        "title_badge": "OPPO A3 Pro 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO A3 Pro 5G៖

📱 ទំហំអេក្រង់៖ 6.7" Curved AMOLED (120Hz, Corning Gorilla Glass Victus 2)
📺 Resolution៖ 1080 x 2412 ភីកសែល (~394 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ តួកាយ 360° Anti-Drop Armor Body | ជម្រើសពណ៌៖ Ocean Blue, Lapis Pink, Mountain Blue (Leather)
🚀 Performance Chip៖ MediaTek Dimensity 7050 (6nm)
⚡ CPU៖ Octa-core (2x2.6 GHz Cortex-A78 + 6x2.0 GHz Cortex-A55)
🧠 RAM៖ 8GB / 12GB
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB UFS 3.1

🌟 ចំណុចពិសេស៖
- ទូរស័ព្ទធន់ខ្លាំង ការពារទឹកកម្រិតខ្ពស់ IP69 / IP68 / IP66 (ធន់នឹងទឹកក្តៅ និងទឹកសម្ពាធខ្ពស់)
- កញ្ចក់អេក្រង់ Victus 2 ធន់នឹងការធ្លាក់ និងការឆ្កូត
- កាមេរ៉ាមេ 64MP AI Main Camera + 2MP Depth
- ថាមពលថ្ម 5000 mAh និងសាកលឿន 67W SUPERVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO A98 5G",
        "slug": "oppo-a98-5g-specifications",
        "image_file": "oppo-a98-5g_cover.png",
        "bg_color": (25, 32, 42),
        "accent_color": (0, 170, 230),
        "title_badge": "OPPO A98 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO A98 5G៖

📱 ទំហំអេក្រង់៖ 6.72" FHD+ LTPS LCD (120Hz Ultra Smooth)
📺 Resolution៖ 1080 x 2400 ភីកសែល (~392 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ឌីហ្សាញ OPPO Glow | ជម្រើសពណ៌៖ Dreamy Blue, Cool Black
🚀 Performance Chip៖ Qualcomm Snapdragon 695 5G (6nm)
⚡ CPU៖ Octa-core (2x2.2 GHz Kryo 660 Gold + 6x1.7 GHz Kryo 660 Silver)
🧠 RAM៖ 8GB (+8GB RAM Expansion)
💾 Storage (ទំហំផ្ទុក)៖ 256GB (គាំទ្រ MicroSD កាតរហូតដល់ 1TB)

🌟 ចំណុចពិសេស៖
- កាមេរ៉ា 40x Microlens ថតមើលវត្ថុទំហំមីក្រូទស្សន៍ច្បាស់លម្អិត
- កាមេរ៉ាមេ 64MP AI Main + 2MP Microlens + 2MP Depth
- ថាមពលថ្ម 5000 mAh ជាមួយសាកលឿន 67W SUPERVOOC (សាក 44 នាទីពេញ)
- ប្រព័ន្ធបំពងសំឡេង Dual Stereo Speakers បង្កើនសំឡេង 200%"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO A79 5G",
        "slug": "oppo-a79-5g-specifications",
        "image_file": "oppo-a79-5g_cover.png",
        "bg_color": (32, 28, 20),
        "accent_color": (220, 180, 60),
        "title_badge": "OPPO A79 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO A79 5G៖

📱 ទំហំអេក្រង់៖ 6.72" Sunlight Display FHD+ (90Hz, 680 nits Peak)
📺 Resolution៖ 1080 x 2400 ភីកសែល (~392 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ ឌីហ្សាញ Feather Green Texture | ជម្រើសពណ៌៖ Mystery Black, Mystery Green
🚀 Performance Chip៖ MediaTek Dimensity 6020 (7nm)
⚡ CPU៖ Octa-core (2x2.2 GHz Cortex-A76 + 6x2.0 GHz Cortex-A55)
🧠 RAM៖ 8GB LPDDR4X
💾 Storage (ទំហំផ្ទុក)៖ 256GB UFS 2.2

🌟 ចំណុចពិសេស៖
- ឌីហ្សាញ Feather Green ស្អាតប្លែកដូចរោមសត្វចែងចាំង
- កាមេរ៉ាមេ 50MP AI Camera + 2MP Portrait Camera
- Dual Stereo Speakers ជាមួយ 300% Ultra Volume Mode
- ថាមពលថ្ម 5000 mAh និងសាកលឿន 33W SUPERVOOC"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ OPPO A58 5G",
        "slug": "oppo-a58-5g-specifications",
        "image_file": "oppo-a58-5g_cover.png",
        "bg_color": (24, 30, 36),
        "accent_color": (0, 190, 160),
        "title_badge": "OPPO A58 5G",
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ OPPO A58 5G៖

📱 ទំហំអេក្រង់៖ 6.56" HD+ Sunlight Display (90Hz Refresh Rate)
📺 Resolution៖ 720 x 1612 ភីកសែល (~269 ppi)
✨ ក្របខ័ណ្ឌ និងជម្រើសពណ៌៖ Silk Satin Texture | ជម្រើសពណ៌៖ Breeze Black, Tranquil Sea Blue, Starry Purple
🚀 Performance Chip៖ MediaTek Dimensity 700 (7nm)
⚡ CPU៖ Octa-core (2x2.2 GHz Cortex-A76 + 6x2.0 GHz Cortex-A55)
🧠 RAM៖ 6GB / 8GB
💾 Storage (ទំហំផ្ទុក)៖ 128GB UFS 2.2

🌟 ចំណុចពិសេស៖
- ឌីហ្សាញរលូន Silk Satin Texture កាន់ស្រួលដៃ មិនស្អិតស្នាមម្រាមដៃ
- កាមេរ៉ាមេ 50MP AI Main + 2MP Depth Camera
- ថាមពលថ្មធំ 5000 mAh និងសាកលឿន 33W SUPERVOOC Fast Charge
- ការពារទឹកកម្រិត IP54 Splash-proof និង Dual Speakers"""
    }
]

def run():
    print(f"Starting seed process for {len(OPPO_BLOG_DATA)} OPPO phone models...")
    count = 0
    for item in OPPO_BLOG_DATA:
        img_rel_path = ensure_image(
            item["image_file"],
            item["title_badge"],
            item["bg_color"],
            item.get("accent_color", (0, 204, 136))
        )
        
        blog_obj, created = Blog.objects.update_or_create(
            slug=item["slug"],
            defaults={
                "name": item["name"],
                "description": item["description"],
                "image": img_rel_path
            }
        )
        action = "Created" if created else "Updated"
        print(f"[{action}] Blog ID {blog_obj.id}: {blog_obj.slug}")
        count += 1
    
    print(f"Successfully populated {count} OPPO blogs into database!")

if __name__ == '__main__':
    run()
