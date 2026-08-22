import re

file_path = r"d:\proj\phone_shop\PNK\accounts\templates\accounts\includes\HeaderSection.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix multiline {{ ... }}
# e.g. {{\n   store_settings... }} -> {{ store_settings... }}
fixed_content = re.sub(r'\{\{\s*\n\s*', '{{ ', content)
fixed_content = re.sub(r'\s*\n\s*\}\}', ' }}', fixed_content)

# Fix multiline {% ... %}
fixed_content = re.sub(r'\{\%\s*\n\s*', '{% ', fixed_content)
fixed_content = re.sub(r'\s*\n\s*\%\}', ' %}', fixed_content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(fixed_content)

print("Cleaned all template tags in HeaderSection.html successfully!")
