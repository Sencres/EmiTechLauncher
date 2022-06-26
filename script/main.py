from git import Git
from os import listdir, path
from shutil import move, rmtree

remoteRepoLink = "https://github.com/Aririi/EmiTech.git"
localRepoPath = ".."
localRepo = Git(localRepoPath)

if path.exists(f"{localRepoPath}/.git") == False:
    localRepo.clone(remoteRepoLink)

    # move everything from cloned repo to instance folder
    for file in listdir(f"{localRepoPath}/EmiTech"):
        if path.exists(path.join(f"{localRepoPath}", file)) == False:
            move(path.join(f"{localRepoPath}/EmiTech", file), localRepoPath)

    # delete ./EmiTech
    try:
        rmtree("{localRepoPath}/EmiTech")
    except OSError as err:
        print(f"Couldn't delete cloned repository: {err.strerror}")
else:
    localRepo.stash("--include-untracked")
    localRepo.pull(remoteRepoLink)
