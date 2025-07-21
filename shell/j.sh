#!/bin/bash 

mkdir f1/f2

if [ $? -eq 0 ]; then 
    echo "success"
else 
    echo "fail"
fi

echo "============="

mkdir -p f1/f2

if [ $? -eq 0 ]; then 
    echo "success"
else 
    echo "fail"
fi