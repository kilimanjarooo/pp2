import re

pattern = re.compile(r"[ ,.]")

text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
print(pattern.sub(":", text))