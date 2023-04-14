import os, sys
music = [file.name for file in os.scandir('.') if file.is_file() and file.name.endswith('.mp3')]
print(music)