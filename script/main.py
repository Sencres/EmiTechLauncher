from subprocess import CalledProcessError, PIPE, run, TimeoutExpired

if platform() == "Linux":
    try:
        ret = run("../scripts/main.sh",
                  shell=True,
                  check=True,
                  stderr=PIPE,
                  timeout=10)
        
        ret.check_returncode()
    except TimeoutExpired:
        print("Unable to open shell script: Connection timed out")
        exit(1)
    except CalledProcessError as err:
        print(("An error occurred in shell script:\n"
               f"Return code: {err.returncode}\n"
               f"Error: {err.stderr.decode('utf-8')}"))
        exit(1)

    exit(0)

from os import environ, makedirs, path, pathsep, remove, system, walk
from pathlib import Path
from shutil import copy, rmtree

scriptPath = Path().resolve().__str__()
# mmc opens script in .minecraft so we replace last occurrence with script
scriptPath = "script".join(scriptPath.rsplit(".minecraft", 1))

gitPath = path.join(scriptPath, "cmd")

# temporarily append git executable folder to path
environ["PATH"] = gitPath + pathsep + environ["PATH"]

from git import Git

remoteRepoLink = "https://github.com/Aririi/EmiTech.git"
localRepoPath = ".."
localRepo = Git(localRepoPath)

if not path.exists(f"{localRepoPath}/.git"):
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
            while not path.exists(dstDir):
                if count == 10:
                    print(f"Copying directory \"{dstDir}\" failed")
                    exit(1)

                makedirs(dstDir)
                count += 1

        for file in files:
            srcFile = path.join(root, file)
            dstFile = path.join(dstDir, file)

            if path.exists(dstFile):
                if path.samefile(srcFile, dstFile):
                    continue
                remove(dstFile)

            count = 0
            # copy(), unlike move(), replaces files if they existž
            while not path.exists(dstFile):
                if count == 10:
                    print(f"Copying file \"{dstFile}\" failed")
                    exit(1)

                copy(srcFile, dstDir)
                count += 1

    # delete cloned repo folder
    try:
        system("cd .. && rmdir /s /q EmiTech")
    except OSError as err:
        print(f"Couldn't delete cloned repository folder: {err.strerror}")
else:
    # crlf being changed to lf pollutes the logs and possibly causes issues
    localRepo.config("core.autocrlf", "false")
    localRepo.add(".")
    print(localRepo.stash())
    print(localRepo.pull(remoteRepoLink))
