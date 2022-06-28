#!/bin/sh
remoteRepoLink="https://github.com/Aririi/EmiTech"
localRepoPath=".."
repoName="EmiTech"

cloneRepo() {
	echo "Cloning $remoteRepoLink to $localRepoPath"
	git clone $remoteRepoLink
	mv $repoName/* $localRepoPath
	mv $repoName/.* $localRepoPath
	touch ./keepme
}

pullRepo() {
	git stash
	git pull
}

#check if first run by looking for file
if ls ./keepme
then
    echo "Repo already cloned, pulling..."
	git pull
else
    echo "First time run, cloning..."
	cloneRepo
fi

