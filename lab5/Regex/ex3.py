import re

pattern = re.compile(r"[a-z]+\_")

print(pattern.findall("Tokugava_Iyeyasu is"))