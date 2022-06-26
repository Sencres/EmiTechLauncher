import git
from git import Git, Repo, RemoteProgress
import os.path
from datetime import datetime
pack_repo = 'https://github.com/Aririi/EmiTech.git'
repo_path = "../"
#repo clone progress function

class CloneProgress(RemoteProgress):
	def update(self, op_code, cur_count, max_count=None, message=''):
		if message:
			print(message)

now = datetime.now()
print("Running at", now)

#Clone repo on first time, determined if git folder exists
git_exists = os.path.exists("../.git")
if (git_exists != True):
	print("First time run, downloading content")
	#borrowed from https://stackoverflow.com/questions/2472552/python-way-to-clone-a-git-repository

	print('Cloning into %s' % pack_repo)
	git.Repo.clone_from(pack_repo, repo_path, 
       branch='master', progress=CloneProgress())
	# class git_operation_clone():
		# try:
			# def __init__(self):
				# self.DIR_NAME = repo_path
				# self.REMOTE_URL = pack_repo

			# def git_clone(self):
				# if os.path.isdir(repo_path):
					# shutil.rmtree(repo_path)
				# os.mkdir(repo_path)
				# repo = git.Repo.init(repo_path)
				# origin = repo.create_remote('origin', pack_repo)
				# origin.fetch()
				# origin.pull(origin.refs[0].remote_head)
		# except Exception as e:
			# print(str(e))

else:
#stashes any changes if a local file has been modified that is in the repo; ideally, the player will sort out this difference manually if they need to
#however, only configs that need to be changed will be pushed, so thhis is unlikely to cause undesired behavior

#making Repo object
	#repo_path = os.getenv('GIT_REPO_PATH')
	repo = Repo(repo_path)
	if not repo.bare:
		print('Repo at {} successfully loaded.'.format(repo_path))
	else:
		print('Could not load repository at {} :('.format(repo_path))
	print(Git("../").status)
	print("Stashing and pulling")
	#git stash --include-untracked
	#Git("../").stash(pack_repo --include-untracked")
	repo.git.stash('save', "--include-untracked")
	#git pull (fetch and merge), should not make any conflicts since changes were stashed
	Git("../").pull(pack_repo)
	print(Git("../").status())