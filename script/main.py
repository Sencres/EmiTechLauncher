from os import environ, path, pathsep
from pathlib import Path
from platform import system as platform

scriptPath = Path().resolve().__str__()
# mmc opens script in .minecraft so we replace last occurrence with script
scriptPath = "script".join(scriptPath.rsplit(".minecraft", 1))

if platform() == "Windows":
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

from os import makedirs, remove, system, walk
from shutil import copy, rmtree

remoteRepoLink = "https://github.com/Aririi/EmiTech.git"
localRepoPath = ".."
localRepo = Git(localRepoPath)

if path.exists(f"{localRepoPath}/.git") == False:
    localRepo.clone(remoteRepoLink)
    # remove temp files
    Git(f"{localRepoPath}/EmiTech").gc("--auto", "--aggressive", "--prune")

    clonedRepoLink = f"{localRepoPath}/EmiTech"
    # walk() goes through folders and subfolders
    for root, dirs, files in walk(clonedRepoLink):
        dstDir = root.replace(clonedRepoLink, f"{localRepoPath}/", 1)
        if not path.exists(dstDir):
            count = 0
            # move() and copy() dont make dest dirs so we gotta make em
            while path.exists(dstDir) == False:
                if count == 10:
                    print(f"Copying directory \"{dstDir}\" failed")
                    exit(1)
                
                makedirs(dstDir)
                count += 1

        for file in files:
            srcFile = path.join(root, file)
            dstFile = path.join(dstDir, file)

            if path.exists(dstFile) and path.samefile(srcFile, dstFile):
                continue

            count = 0
            # copy(), unlike move(), replaces files if they existž
            while path.exists(dstFile) == False:
                if count == 10:
                    print(f"Copying file \"{dstFile}\" failed")
                    exit(1)
                
                copy(srcFile, dstDir)
                count += 1

    # delete cloned repo folder
    try:
        if platform() == "Windows":
            system("cd .. && rmdir /s /q EmiTech")
        elif platform() == "Linux":
            system("cd .. && rm -rfd EmiTech")
        else:
            rmtree(f"{localRepoPath}/EmiTech")
    except OSError as err:
        print(f"Couldn't delete cloned repository folder: {err.strerror}")
else:
    # crlf being changed to lf pollutes the logs and possibly causes issues
    localRepo.config("core.autocrlf", "false")

    pathsToStash = [".minecraft/mods",
                    ".minecraft/config",
                    "LICENSE",
                    "README.md"]
    # stash push only stashes specified files/folders
    # without push it would stash scripts and configs which breaks everything
    localRepo.stash("push", "--quiet", "--include-untracked", *pathsToStash)
    localRepo.pull(remoteRepoLink)
