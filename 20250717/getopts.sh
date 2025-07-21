#!/bin/bash
# getopts.sh檔名

while getopts "abc:d:" opt; do
    case $opt in
    a)
        echo "-a option"
        ;;
    b)
        echo "-b option"
        ;;
    c)
        echo "-c option with argument: $OPTARG"
        ;;
    d)
        echo "-d option with argument: $OPTARG"
        ;;      
    *)
        echo "invalid option: $opt"
        ;;
    esac
done