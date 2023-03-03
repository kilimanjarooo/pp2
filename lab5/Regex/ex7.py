import re

def snakeToCamel(text):
    camel = ""
    pattern = re.compile(r"[_]")
    words = pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camel += word.capitalize()
        else:
            camel += word
    return camel

print(snakeToCamel("hello_world_wordle"))