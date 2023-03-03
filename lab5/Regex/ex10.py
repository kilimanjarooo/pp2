import re

def swap(matchObject):
    return matchObject.group("g1") + "_" + matchObject.group("g2".lower())

text = "mySuperVar"
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"

print(re.sub(pattern, swap, text))