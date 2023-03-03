import re

pattern = re.compile(r"a.+b\Z")

print(pattern.search("anuar1"))
print(pattern.search("2maripov"))
print(pattern.search("kktngtag423b"))

