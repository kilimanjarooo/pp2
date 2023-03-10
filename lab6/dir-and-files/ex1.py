import pathlib
import os

def listDirectories(p):
    print([x.name for x in os.scandir(path = p) if x.is_dir()])

def listFiles(p):
    print([x.name for x in os.scandir(path = p) if x.is_file()])

def listDirectoriesAndFiles(p):
    print([x.name for x in os.scandir(path = p)])

path = '..\..\..\учоба\Linear Algebra and analytical geometry'
listDirectories(path)
listFiles(path)
listDirectoriesAndFiles(path)