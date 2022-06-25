import ctypes
from git import Git
from os import listdir, path, rename, exists
from sys import platform

#dirlist = [item for item in listdir("../") if path.isdir(path.join("../", item))]
#for folder in dirlist:
#    if folder == "git":
#        if platform == "win32":
#            ctypes.windll.kernel32.SetFileAttributesW("../git", 0x02)
#        rename("../git", "../.git")

#Git("../").pull("https://github.com/Sencres013/EmiTech.git --rebase")

print("Running")
#Clone repo on first time, determined if git folder exists
if !(os.path.exists("../.git")):
	print("First time run, downloading content")
	Git.clone_from("https://github.com/Aririi/EmiTech.git", "../", branch="master")
else:
#git stash --include-untracked
#stashes any changes if a local file has been modified that is in the repo; ideally, the player will sort out this difference manually if they need to
#however, only configs that need to be changed will be pushed, so thhis is unlikely to cause undesired behavior
	print(Git("../").status
	print("Stashing and pulling")
	Git("../").stash("https://github.com/Aririi/EmiTech.git --include-untracked")
	Git("../").pull("https://github.com/Sencres013/EmiTech.git")
	print(Git("../").status())