import os
p = (r"C:\Users\Kilimanjaro\Desktop\учоба\Linear Algebra and analytical geometry")

if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")