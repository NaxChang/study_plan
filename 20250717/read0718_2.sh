#!/bin/bash
# read0718_2.sh 檔名
# 目標 file.txt

c=0

while read x y; do
    ((c++))
    echo "${c}: $((x+y))" 
done