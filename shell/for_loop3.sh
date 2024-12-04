#!/bin/bash
# 我要印出`ls`執行完之後的結果,變成for迴圈的方式迭代出來

for i in `ls` ;do 
    echo "result: $i"
done