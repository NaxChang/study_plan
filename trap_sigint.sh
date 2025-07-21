#!/bin/bash
# trap_sigint.sh
trap 'echo "caught SIGINT"' SIGINT SIGTERM

while true; do
    date 
    sleep 3
done
