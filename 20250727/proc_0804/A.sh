#!/bin/bash
# A.sh -> filename


b1_pid=""
b2_pid=""

trap "cleanup" SIGINT

cleanup () {
    kill ${b1_pid}
    kill ${b2_pid}
}

./B.sh &
b1_pid=$!
./B.sh &
b2_pid=$! 

echo "b1_pid: ${b1_pid}"
echo "b2_pid: ${b2_pid}"

wait






