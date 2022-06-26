from git import Git
from os import makedirs, path, remove, walk
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
                continue

            copy(srcFile, dstDir)

    # delete ./EmiTech
    try:
        rmtree(f"{localRepoPath}/EmiTech")
    except OSError as err:
        print(f"Couldn't delete cloned repository: {err.strerror}")
else:
    localRepo.stash("--include-untracked")
    localRepo.pull(remoteRepoLink)
