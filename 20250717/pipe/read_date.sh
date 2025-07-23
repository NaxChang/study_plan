#!/bin/bash
# 檔名:read_date.sh

if [ ! -p mypipe ]; then
    echo "no pipe to read from."
    exit 1 
fi  

while read line; do 
    echo "recieved: ${line}"
done < mypipe