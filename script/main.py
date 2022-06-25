import ctypes
from git import Git
from os import listdir, path, rename
from sys import platform

dirlist = [item for item in listdir("../") if path.isdir(path.join("../", item))]
for folder in dirlist:
    if folder == "git":
        if platform == "win32":
            ctypes.windll.kernel32.SetFileAttributesW("../git", 0x02)
        rename("../git", "../.git")

Git("../").pull("https://github.com/Sencres013/EmiTech.git --rebase")
