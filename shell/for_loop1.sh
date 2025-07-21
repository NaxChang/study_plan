#!/bin/bash  

result=""

for i in {1..5};do 
    if [ -z "$result" ];then 
        result="$i"
    else 
        result="$result,$i"
    fi
done
echo "$result"





