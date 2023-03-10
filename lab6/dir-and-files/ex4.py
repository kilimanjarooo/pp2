import os
f = open(r"C:\Users\Kilimanjaro\Desktop\pp2\gitTest\pp2\lab6\dir-and-files\tex.txt")
cnt = 0
for lines in f:
    cnt += 1
print("files has {} lines".format(cnt))