import os
import sys
import math
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
from PIL import Image, ImageDraw, ImageFont, ImageFilter

MEDIA_BLOGS_DIR = os.path.join('media', 'blogs')
os.makedirs(MEDIA_BLOGS_DIR, exist_ok=True)

# Helper function to create smooth vertical linear gradient
def create_gradient(width, height, top_color, bottom_color):
    base = Image.new('RGB', (width, height), top_color)
    top_r, top_g, top_b = top_color
    bot_r, bot_g, bot_b = bottom_color
    
    draw = ImageDraw.Draw(base)
    for y in range(height):
        r = int(top_r + (bot_r - top_r) * (y / height))
        g = int(top_g + (bot_g - top_g) * (y / height))
        b = int(top_b + (bot_b - top_b) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return base

# Try loading TrueType fonts or fallback
def get_font(size, bold=False):
    font_names = [
        "arialbd.ttf" if bold else "arial.ttf",
        "segoeui.ttf" if not bold else "segoeuib.ttf",
        "tahoma.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    ]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()

def draw_iphone_card(filename, model_title, top_col, bot_col, accent_col, camera_type, island_type, gen_tag):
    W, H = 800, 500
    img = create_gradient(W, H, top_col, bot_col)
    draw = ImageDraw.Draw(img)
    
    # Background decorative geometric elements
    draw.ellipse([450, -100, 900, 350], outline=(255, 255, 255, 25), width=2)
    draw.ellipse([-100, 200, 400, 700], outline=(255, 255, 255, 15), width=2)

    # 1. Draw Phone Mockup on right side (center x = 580, y = 250)
    phone_w, phone_h = 240, 420
    px = 550
    py = 40
    
    # Outer Shadow
    shadow_img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_img)
    s_draw.rounded_rectangle([px - 8, py + 8, px + phone_w + 8, py + phone_h + 12], radius=42, fill=(0, 0, 0, 140))
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(15))
    img.paste(shadow_img, (0, 0), shadow_img)

    # Phone Body Frame
    frame_color = accent_col
    draw.rounded_rectangle([px, py, px + phone_w, py + phone_h], radius=40, fill=frame_color, outline=(255, 255, 255, 180), width=3)
    
    # Screen Bezel
    screen_x = px + 10
    screen_y = py + 10
    screen_w = phone_w - 20
    screen_h = phone_h - 20
    draw.rounded_rectangle([screen_x, screen_y, screen_x + screen_w, screen_y + screen_h], radius=32, fill=(15, 15, 20))

    # Screen Display wallpaper glow
    s_glow = create_gradient(screen_w, screen_h, (top_col[0]//2, top_col[1]//2, top_col[2]//2), (20, 25, 35))
    img.paste(s_glow, (screen_x, screen_y))
    draw = ImageDraw.Draw(img)

    # Notch or Dynamic Island
    if island_type == "notch":
        # Screen notch
        draw.rounded_rectangle([px + phone_w//2 - 35, py + 12, px + phone_w//2 + 35, py + 30], radius=8, fill=(10, 10, 12))
    elif island_type == "dynamic":
        # Dynamic Island pill
        draw.rounded_rectangle([px + phone_w//2 - 32, py + 18, px + phone_w//2 + 32, py + 36], radius=10, fill=(0, 0, 0))
        # Camera sensor dot inside
        draw.ellipse([px + phone_w//2 + 14, py + 23, px + phone_w//2 + 22, py + 31], fill=(12, 18, 40))

    # Camera Module (back preview / top-left of phone back, let's draw camera bump on phone)
    bump_x = px + 22
    bump_y = py + 24
    
    if camera_type == "triple":
        # Pro Triple Camera Bump
        draw.rounded_rectangle([bump_x, bump_y, bump_x + 75, bump_y + 80], radius=20, fill=(frame_color[0]+15, frame_color[1]+15, frame_color[2]+15, 230), outline=(255, 255, 255, 120), width=2)
        # Lens 1 (Top Left)
        draw.ellipse([bump_x + 10, bump_y + 10, bump_x + 36, bump_y + 36], fill=(5, 5, 8), outline=(200, 200, 210), width=2)
        draw.ellipse([bump_x + 16, bump_y + 16, bump_x + 30, bump_y + 30], fill=(25, 45, 80))
        # Lens 2 (Bottom Left)
        draw.ellipse([bump_x + 10, bump_y + 44, bump_x + 36, bump_y + 70], fill=(5, 5, 8), outline=(200, 200, 210), width=2)
        draw.ellipse([bump_x + 16, bump_y + 50, bump_x + 30, bump_y + 64], fill=(25, 45, 80))
        # Lens 3 (Right Center)
        draw.ellipse([bump_x + 42, bump_y + 27, bump_x + 68, bump_y + 53], fill=(5, 5, 8), outline=(200, 200, 210), width=2)
        draw.ellipse([bump_x + 48, bump_y + 33, bump_x + 62, bump_y + 47], fill=(25, 45, 80))
        # Flash
        draw.ellipse([bump_x + 48, bump_y + 12, bump_x + 58, bump_y + 22], fill=(250, 240, 200))
    elif camera_type == "diagonal":
        # Dual Diagonal Bump
        draw.rounded_rectangle([bump_x, bump_y, bump_x + 68, bump_y + 68], radius=18, fill=(frame_color[0]+15, frame_color[1]+15, frame_color[2]+15, 230), outline=(255, 255, 255, 120), width=2)
        # Top-Left Lens
        draw.ellipse([bump_x + 10, bump_y + 10, bump_x + 34, bump_y + 34], fill=(5, 5, 8), outline=(200, 200, 210), width=2)
        draw.ellipse([bump_x + 15, bump_y + 15, bump_x + 29, bump_y + 29], fill=(20, 35, 60))
        # Bottom-Right Lens
        draw.ellipse([bump_x + 34, bump_y + 34, bump_x + 58, bump_y + 58], fill=(5, 5, 8), outline=(200, 200, 210), width=2)
        draw.ellipse([bump_x + 39, bump_y + 39, bump_x + 53, bump_y + 53], fill=(20, 35, 60))
    elif camera_type == "vertical":
        # iPhone 16 Pill Vertical Bump
        draw.rounded_rectangle([bump_x + 12, bump_y, bump_x + 52, bump_y + 82], radius=20, fill=(frame_color[0]+20, frame_color[1]+20, frame_color[2]+20, 240), outline=(255, 255, 255, 140), width=2)
        # Lens 1 Top
        draw.ellipse([bump_x + 18, bump_y + 8, bump_x + 46, bump_y + 36], fill=(5, 5, 8), outline=(220, 220, 230), width=2)
        draw.ellipse([bump_x + 24, bump_y + 14, bump_x + 40, bump_y + 30], fill=(15, 45, 90))
        # Lens 2 Bottom
        draw.ellipse([bump_x + 18, bump_y + 44, bump_x + 46, bump_y + 72], fill=(5, 5, 8), outline=(220, 220, 230), width=2)
        draw.ellipse([bump_x + 24, bump_y + 50, bump_x + 40, bump_y + 66], fill=(15, 45, 90))

    # 2. Draw Left Side Text Content
    font_brand = get_font(20, bold=True)
    font_title = get_font(38, bold=True)
    font_sub = get_font(18, bold=False)
    font_badge = get_font(14, bold=True)

    # Brand Tag
    draw.text((45, 50), "APPLE IPHONE", fill=(255, 255, 255, 200), font=font_brand)

    # Generation Badge (e.g. "SERIES 16" / "SERIES 15")
    badge_w, badge_h = 130, 32
    draw.rounded_rectangle([45, 85, 45 + badge_w, 85 + badge_h], radius=8, fill=(255, 255, 255, 40), outline=(255, 255, 255, 120), width=1)
    draw.text((45 + 14, 85 + 6), gen_tag.upper(), fill=(255, 255, 255), font=font_badge)

    # Model Title
    draw.text((45, 145), model_title, fill=(255, 255, 255), font=font_title)

    # Spec Pill Badges
    specs = ["Super Retina XDR", "Bionic / Pro Chip", "Official Specs"]
    y_pos = 230
    for s in specs:
        draw.rounded_rectangle([45, y_pos, 280, y_pos + 36], radius=18, fill=(0, 0, 0, 60), outline=(255, 255, 255, 50))
        draw.text((65, y_pos + 7), f"• {s}", fill=(240, 240, 245), font=font_sub)
        y_pos += 46

    # Bottom Official Guarantee Tag
    draw.line([(45, 430), (450, 430)], fill=(255, 255, 255, 60), width=1)
    draw.text((45, 442), "100% Verified Technical Specifications", fill=(220, 225, 235), font=get_font(14, bold=False))

    target_filepath = os.path.join(MEDIA_BLOGS_DIR, filename)
    img.save(target_filepath, "PNG", quality=95)
    print(f"Generated distinct card: {filename}")
    return f"blogs/{filename}"

IPHONES_CONFIG = [
    {
        "name": "iPhone 13 mini",
        "slug": "iphone-13-mini-specifications",
        "filename": "iphone-13-mini-distinct.png",
        "top_col": (30, 42, 56),
        "bot_col": (15, 22, 32),
        "accent_col": (90, 110, 130),
        "camera_type": "diagonal",
        "island_type": "notch",
        "gen_tag": "Series 13",
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
        "name": "iPhone 13",
        "slug": "iphone-13-specifications",
        "filename": "iphone-13-distinct.png",
        "top_col": (28, 65, 105),
        "bot_col": (12, 30, 55),
        "accent_col": (65, 120, 180),
        "camera_type": "diagonal",
        "island_type": "notch",
        "gen_tag": "Series 13",
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
        "name": "iPhone 13 Pro",
        "slug": "iphone-13-pro-specifications",
        "filename": "iphone-13-pro-distinct.png",
        "top_col": (72, 112, 134),
        "bot_col": (30, 55, 75),
        "accent_col": (140, 180, 205),
        "camera_type": "triple",
        "island_type": "notch",
        "gen_tag": "Series 13 Pro",
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
        "name": "iPhone 13 Pro Max",
        "slug": "iphone-13-pro-max-specifications",
        "filename": "iphone-13-pro-max-distinct.png",
        "top_col": (40, 68, 60),
        "bot_col": (15, 32, 28),
        "accent_col": (85, 135, 115),
        "camera_type": "triple",
        "island_type": "notch",
        "gen_tag": "Series 13 Pro Max",
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
        "name": "iPhone 14",
        "slug": "iphone-14-specifications",
        "filename": "iphone-14-distinct.png",
        "top_col": (105, 70, 135),
        "bot_col": (45, 25, 65),
        "accent_col": (175, 120, 215),
        "camera_type": "diagonal",
        "island_type": "notch",
        "gen_tag": "Series 14",
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
        "name": "iPhone 14 Plus",
        "slug": "iphone-14-plus-specifications",
        "filename": "iphone-14-plus-distinct.png",
        "top_col": (35, 95, 160),
        "bot_col": (15, 40, 80),
        "accent_col": (90, 160, 235),
        "camera_type": "diagonal",
        "island_type": "notch",
        "gen_tag": "Series 14 Plus",
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
        "name": "iPhone 14 Pro",
        "slug": "iphone-14-pro-specifications",
        "filename": "iphone-14-pro-distinct.png",
        "top_col": (65, 35, 95),
        "bot_col": (25, 10, 40),
        "accent_col": (145, 90, 195),
        "camera_type": "triple",
        "island_type": "dynamic",
        "gen_tag": "Series 14 Pro",
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
        "name": "iPhone 14 Pro Max",
        "slug": "iphone-14-pro-max-specifications",
        "filename": "iphone-14-pro-max-distinct.png",
        "top_col": (40, 30, 50),
        "bot_col": (15, 12, 22),
        "accent_col": (110, 90, 130),
        "camera_type": "triple",
        "island_type": "dynamic",
        "gen_tag": "Series 14 Pro Max",
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
        "name": "iPhone 15",
        "slug": "iphone-15-specifications",
        "filename": "iphone-15-distinct.png",
        "top_col": (230, 140, 175),
        "bot_col": (110, 45, 80),
        "accent_col": (255, 190, 215),
        "camera_type": "diagonal",
        "island_type": "dynamic",
        "gen_tag": "Series 15",
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
        "name": "iPhone 15 Plus",
        "slug": "iphone-15-plus-specifications",
        "filename": "iphone-15-plus-distinct.png",
        "top_col": (45, 140, 125),
        "bot_col": (15, 65, 60),
        "accent_col": (110, 220, 200),
        "camera_type": "diagonal",
        "island_type": "dynamic",
        "gen_tag": "Series 15 Plus",
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
        "name": "iPhone 15 Pro",
        "slug": "iphone-15-pro-specifications",
        "filename": "iphone-15-pro-distinct.png",
        "top_col": (120, 115, 105),
        "bot_col": (50, 48, 45),
        "accent_col": (195, 190, 175),
        "camera_type": "triple",
        "island_type": "dynamic",
        "gen_tag": "Series 15 Pro",
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
        "name": "iPhone 15 Pro Max",
        "slug": "iphone-15-pro-max-specifications",
        "filename": "iphone-15-pro-max-distinct.png",
        "top_col": (35, 55, 80),
        "bot_col": (12, 22, 38),
        "accent_col": (95, 140, 195),
        "camera_type": "triple",
        "island_type": "dynamic",
        "gen_tag": "Series 15 Pro Max",
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
        "name": "iPhone 16",
        "slug": "iphone-16-specifications",
        "filename": "iphone-16-distinct.png",
        "top_col": (40, 60, 170),
        "bot_col": (15, 20, 75),
        "accent_col": (110, 145, 255),
        "camera_type": "vertical",
        "island_type": "dynamic",
        "gen_tag": "Series 16",
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
        "name": "iPhone 16 Plus",
        "slug": "iphone-16-plus-specifications",
        "filename": "iphone-16-plus-distinct.png",
        "top_col": (20, 120, 130),
        "bot_col": (5, 50, 55),
        "accent_col": (70, 215, 220),
        "camera_type": "vertical",
        "island_type": "dynamic",
        "gen_tag": "Series 16 Plus",
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
        "name": "iPhone 16 Pro Max",
        "slug": "iphone-16-pro-max-specifications",
        "filename": "iphone-16-pro-max-distinct.png",
        "top_col": (160, 115, 80),
        "bot_col": (65, 45, 30),
        "accent_col": (235, 180, 135),
        "camera_type": "triple",
        "island_type": "dynamic",
        "gen_tag": "Series 16 Pro Max",
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
    print(f"Updating {len(IPHONES_CONFIG)} blogs with short titles and distinct images...")
    count = 0
    for cfg in IPHONES_CONFIG:
        rel_img_path = draw_iphone_card(
            cfg["filename"],
            cfg["name"],
            cfg["top_col"],
            cfg["bot_col"],
            cfg["accent_col"],
            cfg["camera_type"],
            cfg["island_type"],
            cfg["gen_tag"]
        )
        
        blog_obj, _ = Blog.objects.update_or_create(
            slug=cfg["slug"],
            defaults={
                "name": cfg["name"], # SHORT TITLE (e.g. "iPhone 16 Pro Max")
                "description": cfg["description"],
                "image": rel_img_path
            }
        )
        print(f"Updated blog {blog_obj.id}: title='{blog_obj.name}' image='{rel_img_path}'")
        count += 1
    
    # Optionally remove non-series old test blogs if present
    Blog.objects.filter(slug__in=['iphone_13_pro', 'iphone_15_blue']).delete()
    print("Cleaned up old test entries!")
    print("Done successfully!")

if __name__ == '__main__':
    run()
