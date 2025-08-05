#!/bin/bash
# B.sh -> filename

s_pid=""

trap "cleanup" SIGINT SIGTERM

cleanup () {
    kill ${s_pid} 
}

sleep 120 &
s_pid=$!

echo "s_pid: ${s_pid}"

wait


