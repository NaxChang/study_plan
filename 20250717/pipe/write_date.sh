#!/bin/bash
# file_name:write_date.sh

mkfifo mypipe 

echo "$(date)" > mypipe



