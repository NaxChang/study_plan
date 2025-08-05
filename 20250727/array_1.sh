#!/bin/bash
# array_1.sh -> filename

declare -a arry

arry=(apple book cat)

declare -a arry
arry=(apple book cat)

index=$1 

if [[ -z "${arry[$index]}" ]]; then
    echo "error: index not found" >&2 
    exit 1
fi

echo "${arry[$index]}"
