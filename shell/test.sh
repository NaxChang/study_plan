#!/bin/bash 

read -p "your branch: " branch
if [ $branch == "main" ] || [ $branch == "master" ];then
    echo "This is our branch"
elif [ $branch == "dev" ];then
    echo "This is a dev branch"
else
    echo "This is a different branch"    
fi    