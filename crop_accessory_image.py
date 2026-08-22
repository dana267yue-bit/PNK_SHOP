import os
from PIL import Image

img_path = r"D:\proj\phone_shop\PNK\media\products\apple1.jpg"
if os.path.exists(img_path):
    img = Image.open(img_path)
    print("Image format:", img.format)
    print("Image size (width x height):", img.size)
    print("Image mode:", img.mode)

    # Let's crop into 4 items
    w, h = img.size
    # Item 1: MagSafe Charger (0 to 0.28)
    crop1 = img.crop((0, 0, int(w * 0.28), h))
    crop1.save(r"D:\proj\phone_shop\PNK\media\products\magsafe_charger.jpg")

    # Item 2: AirTags (0.23 to 0.35)
    crop2 = img.crop((int(w * 0.22), 0, int(w * 0.35), h))
    crop2.save(r"D:\proj\phone_shop\PNK\media\products\airtags.jpg")

    # Item 3: Beats Fit Pro (0.33 to 0.65)
    crop3 = img.crop((int(w * 0.32), 0, int(w * 0.65), h))
    crop3.save(r"D:\proj\phone_shop\PNK\media\products\beats_earbuds.jpg")

    # Item 4: Belkin 3-in-1 (0.65 to 1.0)
    crop4 = img.crop((int(w * 0.65), 0, w, h))
    crop4.save(r"D:\proj\phone_shop\PNK\media\products\belkin_3in1.jpg")

    print("Successfully cropped apple1.jpg into 4 individual accessory images!")
