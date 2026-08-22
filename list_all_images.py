import os

media_dir = r"D:\proj\phone_shop\PNK\media"
for root, dirs, files in os.walk(media_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.svg')):
            rel = os.path.relpath(os.path.join(root, f), media_dir)
            print(rel.replace('\\', '/'))
