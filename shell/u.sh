#!/bin/bash 
# count: 1--------顯示到count: 5
# until迴圈
count=1 
until [ $count -gt 5 ]; do
    echo "count: ${count}"
    count=$((count+1))
done


