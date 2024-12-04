#!/bin/bash  
#ans => 1,2,3,4,5

result=""

for i in {1..5};do
    result=$result$i,
done
echo "${result%,}"




