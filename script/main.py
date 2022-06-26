from os import environ, path, pathsep
from pathlib import Path
from platform import system

if system() == "Windows":
    scriptPath = Path().resolve().__str__()
    # mmc opens script in .minecraft so we replace last occurrence with script
    scriptPath = "script".join(scriptPath.rsplit(".minecraft", 1))
    
    gitPath = path.join(scriptPath, "cmd")
    
    # temporarily append git executable folder to path
    environ["PATH"] = gitPath + pathsep + environ["PATH"]

    from git import Git
else:
    try:
        from git import Git
    except ImportError:
        print("You must have git installed on your machine")
        exit(1)

from os import makedirs, remove, walk
from shutil import copy, rmtree

remoteRepoLink = "https://github.com/Aririi/EmiTech.git"
localRepoPath = ".."
localRepo = Git(localRepoPath)

if path.exists(f"{localRepoPath}/.git") == False:
    localRepo.clone(remoteRepoLink)

    clonedRepoLink = f"{localRepoPath}/EmiTech"
    # walk() goes through folders and subfolders
    for root, dirs, files in walk(clonedRepoLink):
        dstDir = root.replace(clonedRepoLink, f"{localRepoPath}/", 1)
        if not path.exists(dstDir):
            # move() and copy() dont make dest dirs so we gotta make em
            makedirs(dstDir)

        for file in files:
            srcFile = path.join(root, file)
            dstFile = path.join(dstDir, file)

            if path.exists(dstFile) and path.samefile(srcFile, dstFile):
                remove(srcFile)
                continue

            # copy(), unlike move(), replaces files if they exist
            copy(srcFile, dstDir)
            remove(srcFile)

    # delete cloned repo folder
    try:
        rmtree(f"{localRepoPath}/EmiTech")
    except OSError as err:
        print(f"Couldn't delete cloned repository: {err.strerror}")
else:
    # crlf being changed to lf pollutes the logs and possibly causes issues
    localRepo.config("core.autocrlf", "false")
    localRepo.stash("--include-untracked")
    localRepo.pull(remoteRepoLink)
