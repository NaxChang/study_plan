#!/bin/bash
# vars.sh 記好檔名

source config # 放變數
source abc.sh
export var_1 var_2
./b.sh 
echo "source: ($$)"
echo ${var_1}, ${var_2}
