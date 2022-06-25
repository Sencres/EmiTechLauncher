#import ctypes
from git import Git, Repo
#from os import listdir, path, rename, exists
import os.path
#from sys import platform
from datetime import datetime

#dirlist = [item for item in listdir("../") if path.isdir(path.join("../", item))]
#for folder in dirlist:
#    if folder == "git":
#        if platform == "win32":
#            ctypes.windll.kernel32.SetFileAttributesW("../git", 0x02)
#        rename("../git", "../.git")

#Git("../").pull("https://github.com/Sencres013/EmiTech.git --rebase")

now = datetime.now()
print("Running at", now)
#Clone repo on first time, determined if git folder exists
git_exists = os.path.exists("../.git")
if (git_exists != True):
	print("First time run, downloading content")
	Git.clone_from("https://github.com/Aririi/EmiTech.git", "../", branch="master")
else:
#stashes any changes if a local file has been modified that is in the repo; ideally, the player will sort out this difference manually if they need to
#however, only configs that need to be changed will be pushed, so thhis is unlikely to cause undesired behavior

#making Repo object
	#repo_path = os.getenv('GIT_REPO_PATH')
	repo_path = "../"
	repo = Repo(repo_path)
	if not repo.bare:
		print('Repo at {} successfully loaded.'.format(repo_path))
	else:
		print('Could not load repository at {} :('.format(repo_path))
	print(Git("../").status)
	print("Stashing and pulling")
	#git stash --include-untracked
	#Git("../").stash("https://github.com/Aririi/EmiTech.git --include-untracked")
	repo.git.stash('save', "--include-untracked")
	#git pull (fetch and merge), should not make any conflicts since changes were stashed
	Git("../").pull("https://github.com/Aririi/EmiTech.git")
	print(Git("../").status())