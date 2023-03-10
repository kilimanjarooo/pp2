import os
p=(r"C:\Users\Kilimanjaro\Desktop\pp2\gitTest\pp2\lab6\dir-and-files\delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")