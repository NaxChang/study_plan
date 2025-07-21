#!/bin/bash
# read0718_1.sh 檔名
# 目標 file.txt

c=0 

while read a b; do 
    ((c++))
    echo "${c}: ${a}, ${b}"
done

echo ${c}