#!/bin/bash
# pos_1.sh 檔名

for x in "$*"; do   
    echo "argument: $x"
done

echo "number of arguments: $#"