#!/bin/bash -e

echo faucet `git remote get-url faucet`
echo origin `git remote get-url origin`
echo pperry `git remote get-url perry`

fetch="git fetch --tags"
glog="git log -n 1 --pretty=oneline"

for repo in faucet origin perry; do
    for branch in master gmaster; do
	if [ $repo != faucet -o $branch != gmaster ]; then
	    echo Updating $repo $branch
	    $fetch $repo $branch
	    $glog $repo/$branch
	fi
    done
done

# FaucetSDN doesn't use annotated tags for their versions...
mtag=`git describe --tags --abbrev=0 perry/master`
gtag=`git describe --abbrev=0 perry/gmaster`

echo Checking remote master tag $mtag
fm=`git ls-remote faucet $mtag`
om=`git ls-remote origin $mtag`
pm=`git ls-remote perry $mtag`

if [ "$fm" != "$om" ]; then
    echo faucet master: $fm
    echo origin master: $om
    false
fi

if [ "$fm" != "$pm" ]; then
    echo faucet master: $fm
    echo pperry master: $pm
    false
fi

if [ -z "$om" ]; then
    echo Unknown tag $mtag
    false
fi

echo Checking remote gmaster tag $gtag
og=`git ls-remote origin $gtag`
pg=`git ls-remote perry $gtag`

if [ "$og" != "$pg" ]; then
    echo origin gmaster: $og
    echo pperry gmaster: $pg
    false
fi

if [ -z "$og" ]; then
    echo Unknown tag $gtag
    false
fi

mbase=`git merge-base $gtag $mtag`
mref=`git rev-list -n 1 $mtag`
if [ "$mbase" != "$mref" ]; then
    echo
    echo Error:
    echo "  git merge-base $mtag $gtag"
    echo does not match expected $mtag
    echo
    false
fi

echo
echo All remote tags check out.
