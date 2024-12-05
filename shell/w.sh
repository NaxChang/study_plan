#!/bin/bash 
# count: 1--------顯示到count: 5

count=1 
while [ $count -le 5 ]; do
    echo "count: ${count}"
    count=$((count+1))
done


