import os
import sys
import shutil
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    django.setup()
except Exception:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'PNK.settings'
    django.setup()

from shop.models import Blog
from PIL import Image, ImageDraw, ImageFont

MEDIA_BLOGS_DIR = os.path.join('media', 'blogs')
os.makedirs(MEDIA_BLOGS_DIR, exist_ok=True)

# Generate attractive banner image if custom image doesn't exist
def ensure_image(filename, model_slug, color_bg, text_color=(255, 255, 255)):
    target_path = os.path.join(MEDIA_BLOGS_DIR, filename)
    if os.path.exists(target_path):
        return f"blogs/{filename}"
    
    # Check if we can copy from existing product images
    existing_map = {
        'iphone-13': 'ipone_13.png',
        'iphone-13-mini': 'ip13_Black.png',
        'iphone-13-pro': 'ipone_13.png',
        'iphone-13-pro-max': 'ipone_13.png',
        'iphone-14': 'iphone15.jpg',
        'iphone-14-plus': 'iphone15.jpg',
        'iphone-14-pro': 'ipone15_pro.png',
        'iphone-14-pro-max': 'ipone15_pro.png',
        'iphone-15': 'refurb-iphone-15-blue-202412.jpg',
        'iphone-15-plus': 'refurb-iphone-15-blue-202412.jpg',
        'iphone-15-pro': 'Iphone_15_Pro_2.png',
        'iphone-15-pro-max': 'Iphone_15_Pro_2.png',
        'iphone-16': 'refurb-iphone-15-blue-202412.jpg',
        'iphone-16-plus': 'refurb-iphone-15-blue-202412.jpg',
        'iphone-16-pro-max': 'Iphone_15_Pro_2.png',
    }
    
    if model_slug in existing_map:
        source_name = existing_map[model_slug]
        for src_folder in [MEDIA_BLOGS_DIR, os.path.join('media', 'products')]:
            src_path = os.path.join(src_folder, source_name)
            if os.path.exists(src_path):
                shutil.copy(src_path, target_path)
                return f"blogs/{filename}"

    # Generate stylish image using PIL
    img = Image.new('RGB', (800, 500), color=color_bg)
    draw = ImageDraw.Draw(img)
    
    # Add subtle border & text styling
    draw.rectangle([15, 15, 785, 485], outline=(255, 255, 255), width=2)
    
    label = model_slug.replace('-', ' ').title()
    text = f"Apple {label}\nSpecifications & Features"
    draw.text((400, 240), text, fill=text_color, anchor="mm", align="center")
    
    img.save(target_path)
    return f"blogs/{filename}"

IPHONE_DATA = [
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 13 mini",
        "slug": "iphone-13-mini-specifications",
        "image_file": "iphone-13-mini_cover.png",
        "bg_color": (35, 43, 56),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 13 mini៖

📱 ទំហំអេក្រង់៖ 5.4 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1080 x 2340 ភីកសែល (~476 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Glass, ក្របខ័ណ្ឌ អាលុយមីញ៉ូម (Aluminum) | ជម្រើសពណ៌៖ Starlight, Midnight, Blue, Pink, Red, Green
🚀 Performance Chip៖ Apple A15 Bionic (5nm)
⚡ CPU៖ Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)
🧠 RAM៖ 4GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- ទំហំតូចច្រឡឹង 5.4 អ៊ីញ ងាយស្រួលកាន់ និងប្រើប្រាស់ដោយដៃម្ខាង
- ប្រព័ន្ធកាមេរ៉ាភ្លោះ 12MP ជាមួយបច្ចេកវិទ្យា Sensor-shift OIS
- មុខងារ Cinematic Mode ថតវីដេអូព្រិលខ្នងបែបភាពយន្ត
- ថាមពលថ្មប្រសើរជាង iPhone 12 mini រហូតដល់ 1.5 ម៉ោង
- ការពារទឹក និងធូលីកម្រិត IP68"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 13",
        "slug": "iphone-13-specifications",
        "image_file": "iphone-13_cover.png",
        "bg_color": (41, 67, 92),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 13៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1170 x 2532 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Glass, ក្របខ័ណ្ឌ អាលុយមីញ៉ូម | ជម្រើសពណ៌៖ Starlight, Midnight, Blue, Pink, Red, Green
🚀 Performance Chip៖ Apple A15 Bionic (5nm)
⚡ CPU៖ Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)
🧠 RAM៖ 4GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- អេក្រង់ភ្លឺច្បាស់ Super Retina XDR Peak brightness 1200 nits (HDR)
- កាមេរ៉ាមុំទ្រង់ទ្រាយអង្កត់ទ្រូង Diagonal camera layout ជាមួយ Sensor-shift OIS
- មុខងារ Cinematic Mode 1080p 30fps
- ថាមពលថ្មធន់ ប្រើប្រាស់បានយូរជាង iPhone 12 រហូតដល់ 2.5 ម៉ោង
- ល្បឿនអ៊ីនធឺណិត 5G លឿនរហ័ស"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 13 Pro",
        "slug": "iphone-13-pro-specifications",
        "image_file": "iphone-13-pro_cover.png",
        "bg_color": (54, 73, 88),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 13 Pro៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ Super Retina XDR OLED, ProMotion 120Hz
📺 Resolution៖ 1170 x 2532 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Textured Matte Glass, ក្របខ័ណ្ឌ ដែកថែបមិនច្រេះ (Stainless Steel) | ជម្រើសពណ៌៖ Graphite, Gold, Silver, Sierra Blue, Alpine Green
🚀 Performance Chip៖ Apple A15 Bionic (5nm) ជាមួយ 5-core GPU
⚡ CPU៖ Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- អេក្រង់ ProMotion 120Hz រលូនខ្លាំង ស្វ័យប្រវត្តិ 10Hz-120Hz
- កាមេរ៉ា 3 គ្រាប់ (Wide, Ultra Wide, Telephoto 3x)
- សមត្ថភាពថតរូបជិតបំផុត Macro Photography 2cm
- ទ្រទ្រង់ការថតវីដេអូកម្រិតអាជីព ProRes 4K
- LiDAR Scanner សម្រាប់ AR និងថតរូបយប់ Night Mode Portrait"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 13 Pro Max",
        "slug": "iphone-13-pro-max-specifications",
        "image_file": "iphone-13-pro-max_cover.png",
        "bg_color": (30, 48, 64),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 13 Pro Max៖

📱 ទំហំអេក្រង់៖ 6.7 អ៊ីញ Super Retina XDR OLED, ProMotion 120Hz
📺 Resolution៖ 1284 x 2778 ភីកសែល (~458 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Textured Matte Glass, ក្របខ័ណ្ឌ Stainless Steel | ជម្រើសពណ៌៖ Graphite, Gold, Silver, Sierra Blue, Alpine Green
🚀 Performance Chip៖ Apple A15 Bionic (5nm) ជាមួយ 5-core GPU
⚡ CPU៖ Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- អេក្រង់ធំ 6.7 អ៊ីញ ProMotion 120Hz បង្ហាញរូបភាពត្រជាក់ភ្នែក
- ថាមពលថ្មកំពូលធន់បំផុត អាចទស្សនាវីដេអូរហូតដល់ 28 ម៉ោង
- ប្រព័ន្ធកាមេរ៉ា Pro 3 គ្រាប់ ថតរូបពន្លឺខ្សោយបានល្អឥតខ្ចោះ
- Telephoto 3x Optical Zoom & Macro Photography
- ProRes video recording និង LiDAR Scanner"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 14",
        "slug": "iphone-14-specifications",
        "image_file": "iphone-14_cover.png",
        "bg_color": (70, 52, 86),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 14៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1170 x 2532 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Glass, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Midnight, Purple, Starlight, Blue, Red, Yellow
🚀 Performance Chip៖ Apple A15 Bionic (5nm) ជាមួយ 5-core GPU
⚡ CPU៖ Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- មុខងារ Crash Detection ជូនដំណឹងអាសន្នពេលមានគ្រោះថ្នាក់ចរាចរណ៍
- Photonic Engine បង្កើនព័ត៌មានលម្អិត និងពណ៌រូបថតក្នុងពន្លឺទាប
- Action Mode ថតវីដេអូរលូនឥតទប់ជើងកាមេរ៉ា
- RAM កើនឡើងដល់ 6GB ជួយឱ្យ multitasking កាន់តែរលូន
- សុវត្ថិភាពសង្គ្រោះបន្ទាន់ Emergency SOS via satellite"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 14 Plus",
        "slug": "iphone-14-plus-specifications",
        "image_file": "iphone-14-plus_cover.png",
        "bg_color": (88, 59, 99),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 14 Plus៖

📱 ទំហំអេក្រង់៖ 6.7 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1284 x 2778 ភីកសែល (~458 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Glass, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Midnight, Purple, Starlight, Blue, Red, Yellow
🚀 Performance Chip៖ Apple A15 Bionic (5nm) ជាមួយ 5-core GPU
⚡ CPU៖ Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- អេក្រង់ធំ 6.7 អ៊ីញ ផ្តល់បទពិសោធន៍ទស្សនា និងលេងហ្គេមទូលំទូលាយ
- ថាមពលថ្មធំ ប្រើប្រាស់បានយូរអង្វែងពេញមួយថ្ងៃ
- Photonic Engine, Action Mode និង Crash Detection
- ទម្ងន់ស្រាលជាងម៉ូដែល Pro Max (ត្រឹមតែ 203g)
- ប្រព័ន្ធត្រជាក់ខាងក្នុងរៀបចំឡើងវិញ thermal performance ប្រសើរជាងមុន"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 14 Pro",
        "slug": "iphone-14-pro-specifications",
        "image_file": "iphone-14-pro_cover.png",
        "bg_color": (46, 38, 59),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 14 Pro៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ LTPO Super Retina XDR OLED, ProMotion 120Hz, Always-On Display
📺 Resolution៖ 1179 x 2556 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Textured Matte Glass, ក្របខ័ណ្ឌ Stainless Steel | ជម្រើសពណ៌៖ Space Black, Silver, Gold, Deep Purple
🚀 Performance Chip៖ Apple A16 Bionic (4nm)
⚡ CPU៖ Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- Dynamic Island ផ្លាស់ប្តូររបៀបអន្តរកម្មកាមេរ៉ាមុខ និងការជូនដំណឹង
- កាមេរ៉ាមេ 48MP ដំបូងគេ ផ្តល់ទិន្នន័យរូបថត ProRAW ច្បាស់លម្អិត
- អេក្រង់ភ្លឺខ្លាំងរហូតដល់ 2000 nits ពេលប្រើប្រាស់ក្រៅផ្ទះ
- Always-On Display បង្ហាញម៉ោង និង Notification ជានិច្ច
- Action Mode ថតវីដេអូ និង Crash Detection"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 14 Pro Max",
        "slug": "iphone-14-pro-max-specifications",
        "image_file": "iphone-14-pro-max_cover.png",
        "bg_color": (32, 28, 42),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 14 Pro Max៖

📱 ទំហំអេក្រង់៖ 6.7 អ៊ីញ LTPO Super Retina XDR OLED, ProMotion 120Hz, Always-On Display
📺 Resolution៖ 1290 x 2796 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Textured Matte Glass, ក្របខ័ណ្ឌ Stainless Steel | ជម្រើសពណ៌៖ Space Black, Silver, Gold, Deep Purple
🚀 Performance Chip៖ Apple A16 Bionic (4nm)
⚡ CPU៖ Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- Dynamic Island លើអេក្រង់ធំ 6.7 អ៊ីញ
- កាមេរ៉ា 48MP Pro Camera System + 3x Telephoto Zoom
- ថាមពលថ្មធន់បំផុត ទស្សនាវីដេអូបានរហូតដល់ 29 ម៉ោង
- ភាពភ្លឺអេក្រង់កំពូល 2000 nits Peak Brightness
- Always-On Display, Action Mode & Emergency SOS via Satellite"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 15",
        "slug": "iphone-15-specifications",
        "image_file": "iphone-15_cover.png",
        "bg_color": (44, 76, 92),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 15៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1179 x 2556 ភីកសែល (~461 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Color-infused Glass, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Black, Blue, Green, Yellow, Pink
🚀 Performance Chip៖ Apple A16 Bionic (4nm)
⚡ CPU៖ Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- បំពាក់ Dynamic Island លើម៉ូដែល standard ដំបូងគេ
- រន្ធសាក USB Type-C ជំនួស Lightning port
- កាមេរ៉ាមេ 48MP ថតរូបកម្រិត 24MP default & 2x Telephoto Zoom
- ខ្នងកញ្ចក់ប្រភេទ Color-infused glass មានពណ៌ស្រស់ស្អាតប្លែក
- គែមតួកាយមូល Contour edges កាន់ស្រួលដៃ"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 15 Plus",
        "slug": "iphone-15-plus-specifications",
        "image_file": "iphone-15-plus_cover.png",
        "bg_color": (38, 84, 86),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 15 Plus៖

📱 ទំហំអេក្រង់៖ 6.7 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1290 x 2796 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Color-infused Glass, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Black, Blue, Green, Yellow, Pink
🚀 Performance Chip៖ Apple A16 Bionic (4nm)
⚡ CPU៖ Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)
🧠 RAM៖ 6GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- អេក្រង់ធំ 6.7 អ៊ីញ ជាមួយ Dynamic Island
- រន្ធសាក USB Type-C ងាយស្រួលប្រទាក់ជាមួយឧបករណ៍ដទៃ
- កាមេរ៉ាមេ 48MP ថតរូបច្បាស់ និង Telephoto 2x គុណភាពខ្ពស់
- ថាមពលថ្មកំពូល ប្រើប្រាស់បានយូរបំផុតក្នុងត្រកូល iPhone 15
- Roadside Assistance via satellite & Crash Detection"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 15 Pro",
        "slug": "iphone-15-pro-specifications",
        "image_file": "iphone-15-pro_cover.png",
        "bg_color": (50, 52, 58),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 15 Pro៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ LTPO Super Retina XDR OLED, ProMotion 120Hz, Always-On Display
📺 Resolution៖ 1179 x 2556 ភីកសែល (~461 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Matte Glass, ក្របខ័ណ្ឌ Titanium Grade 5 | ជម្រើសពណ៌៖ Black Titanium, White Titanium, Blue Titanium, Natural Titanium
🚀 Performance Chip៖ Apple A17 Pro (3nm)
⚡ CPU៖ Hexa-core (2x3.78 GHz + 4x2.11 GHz)
🧠 RAM៖ 8GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- តួកាយធ្វើពី Titanium Grade 5 ស្រាល និងរឹងមាំខ្លាំង
- ប៊ូតុង Action Button អាចកំណត់មុខងារ (Customizable Shortcuts)
- ឈីប Apple A17 Pro 3nm ដំបូងគេ គាំទ្រ Hardware-accelerated Ray Tracing លេងហ្គេម Console
- រន្ធសាក USB-C 3.0 ល្បឿនផ្ទេរទិន្នន័យ 10Gbps
- ថតវីដេអូ ProRes 4K 60fps ផ្ទាល់ទៅកាន់ External Storage"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 15 Pro Max",
        "slug": "iphone-15-pro-max-specifications",
        "image_file": "iphone-15-pro-max_cover.png",
        "bg_color": (34, 37, 43),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 15 Pro Max៖

📱 ទំហំអេក្រង់៖ 6.7 អ៊ីញ LTPO Super Retina XDR OLED, ProMotion 120Hz, Always-On Display
📺 Resolution៖ 1290 x 2796 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ កញ្ចក់ Ceramic Shield ខាងមុខ, ខ្នងកញ្ចក់ Matte Glass, ក្របខ័ណ្ឌ Titanium Grade 5 | ជម្រើសពណ៌៖ Black Titanium, White Titanium, Blue Titanium, Natural Titanium
🚀 Performance Chip៖ Apple A17 Pro (3nm)
⚡ CPU៖ Hexa-core (2x3.78 GHz + 4x2.11 GHz)
🧠 RAM៖ 8GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- ក្របខ័ណ្ឌ Titanium ស្រាលជាងមុន ជាមួយ Bezel ស្តើងបំផុត
- កាមេរ៉ា 5x Optical Zoom (Tetraprism Lens) ថតចម្ងាយឆ្ងាយច្បាស់
- Action Button កំណត់ shortcut តាមចង់បាន
- ឈីប A17 Pro 3nm ល្បឿនលឿន និងសន្សំសំចៃថាមពល
- ទំហំផ្ទុកចាប់ផ្តើមពី 256GB និងរន្ធ USB-C 3.0 10Gbps"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 16",
        "slug": "iphone-16-specifications",
        "image_file": "iphone-16_cover.png",
        "bg_color": (24, 72, 85),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 16៖

📱 ទំហំអេក្រង់៖ 6.1 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1179 x 2556 ភីកសែល (~461 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ Ceramic Shield ជំនាន់ថ្មី ខាងមុខ, ខ្នងកញ្ចក់ Color-infused Glass, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Black, White, Pink, Teal, Ultramarine
🚀 Performance Chip៖ Apple A18 (3nm)
⚡ CPU៖ Hexa-core (2x4.04 GHz + 4x2.20 GHz)
🧠 RAM៖ 8GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- ប៊ូតុងបញ្ជាកាមេរ៉ាថ្មី Camera Control ប៉ះបញ្ជា Zoom, Focus & Exposure
- ទ្រទ្រង់ប្រព័ន្ធប្រាជ្ញាសិប្បនិម្មិត Apple Intelligence
- ប៊ូតុង Action Button លើកដំបូងសម្រាប់ម៉ូដែល Standard
- កាមេរ៉ាមេ 48MP Fusion ថត Spatial Photos & Videos សម្រាប់ Apple Vision Pro
- ឈីប A18 (3nm) លឿនរហ័ស និង RAM 8GB"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 16 Plus",
        "slug": "iphone-16-plus-specifications",
        "image_file": "iphone-16-plus_cover.png",
        "bg_color": (28, 88, 96),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 16 Plus៖

📱 ទំហំអេក្រង់៖ 6.7 អ៊ីញ Super Retina XDR OLED
📺 Resolution៖ 1290 x 2796 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ Ceramic Shield ជំនាន់ថ្មី ខាងមុខ, ខ្នងកញ្ចក់ Color-infused Glass, ក្របខ័ណ្ឌ Aluminum | ជម្រើសពណ៌៖ Black, White, Pink, Teal, Ultramarine
🚀 Performance Chip៖ Apple A18 (3nm)
⚡ CPU៖ Hexa-core (2x4.04 GHz + 4x2.20 GHz)
🧠 RAM៖ 8GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 128GB / 256GB / 512GB

🌟 ចំណុចពិសេស៖
- អេក្រង់ធំ 6.7 អ៊ីញ ពណ៌ស្រស់ត្រកាល
- ប៊ូតុង Camera Control និង Action Button
- ទ្រទ្រង់ Apple Intelligence បង្កើនប្រសិទ្ធភាពការងារ
- ថាមពលថ្មប្រើប្រាស់បានយូរអស្ចារ្យ
- កាមេរ៉ា 48MP Fusion និងថត Spatial Audio / Spatial Video"""
    },
    {
        "name": "ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសនៃ iPhone 16 Pro Max",
        "slug": "iphone-16-pro-max-specifications",
        "image_file": "iphone-16-pro-max_cover.png",
        "bg_color": (45, 42, 38),
        "description": """ព័ត៌មានលម្អិត និងលក្ខណៈបច្ចេកទេសផ្លូវការរបស់ iPhone 16 Pro Max៖

📱 ទំហំអេក្រង់៖ 6.9 អ៊ីញ LTPO Super Retina XDR OLED, ProMotion 120Hz, Always-On Display
📺 Resolution៖ 1320 x 2868 ភីកសែល (~460 ppi)
✨ កញ្ចក់ និងជម្រើសពណ៌៖ Ceramic Shield ជំនាន់ចុងក្រោយ ខាងមុខ, ក្របខ័ណ្ឌ Titanium Grade 5 | ជម្រើសពណ៌៖ Black Titanium, White Titanium, Natural Titanium, Desert Titanium
🚀 Performance Chip៖ Apple A18 Pro (3nm)
⚡ CPU៖ Hexa-core (2x4.04 GHz + 4x2.20 GHz)
🧠 RAM៖ 8GB NVMe
💾 Storage (ទំហំផ្ទុក)៖ 256GB / 512GB / 1TB

🌟 ចំណុចពិសេស៖
- អេក្រង់ធំបំផុត 6.9 អ៊ីញ ជាមួយ Bezel ស្តើងបំផុតក្នុងប្រវត្តិសាស្ត្រ iPhone
- ប៊ូតុង Camera Control និងកាមេរ៉ា 48MP Ultra Wide ជំនាន់ថ្មី
- ថតវីដេអូ 4K 120fps Dolby Vision រលូនបំផុត
- ឈីប Apple A18 Pro (3nm) កំពូលល្បឿន និង Neural Engine 16-core
- ទ្រទ្រង់ Apple Intelligence ពេញលេញ និងថ្មប្រើបានយូរបំផុត"""
    }
]

def run():
    print(f"Starting seed process for {len(IPHONE_DATA)} iPhone models...")
    count = 0
    for item in IPHONE_DATA:
        model_slug = item["slug"].replace('-specifications', '')
        img_rel_path = ensure_image(item["image_file"], model_slug, item["bg_color"])
        
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
    
    print(f"Successfully populated {count} iPhone blogs into database!")

if __name__ == '__main__':
    run()
