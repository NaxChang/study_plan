#!/bin/bash
# getopts_1.sh檔名

var_a=""
var_b=""
do_calc="n"

while getopts "a:b:c" opt; do
    case $opt in
        a)
            var_a="$OPTARG"
            ;;
        b)
            var_b="$OPTARG"
            ;;
        c)
            do_calc="y"
            ;;
        *)
            exit 1
            ;;
    esac
done

if [ "$do_calc" = "y" ]; then
    sum=$(( $var_a + $var_b ))
    echo "a: ${var_a} b: ${var_b} sum: ${sum}"
else
    echo "a: ${var_a} b: ${var_b}"
fi






        


    
