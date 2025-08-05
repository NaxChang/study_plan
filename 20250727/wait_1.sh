#!/bin/bash
# wait_1.sh -> filename

# 計算從 1 加到 $1（第一個參數）的總和，
# 並且顯示目前這個 Shell 行程的 PID，以及運算結果。

calc () {
    echo "PID $$ started."
    n=$1
    sum=0
    for (( i=1; i<=n; i++ )); do
        (( sum += i))
    done
    echo "Sum ${sum}"
}

calc 5 & p1=$!
echo "1-5"
calc 10 & p2=$!
echo "1-10"
calc 20 & p3=$!
echo "1-20"
wait

echo "Done: $p1 $p2 $p3"
echo "ALL Done"