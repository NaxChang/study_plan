#!/bin/bash
# trap_sigint1.sh

clean_func () {
    echo "cleaning"
}

trap 'echo "finish"; clean_func' EXIT 

echo "test"
