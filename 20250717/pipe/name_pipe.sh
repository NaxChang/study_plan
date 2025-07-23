#!/bin/bash
# 20250717/ file_name:name_pipe.sh

mkfifo mypipe

ls -lh mypipe 

echo "hello" > mypipe &

sleep 3

cat mypipe

