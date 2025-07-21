#!/bin/bash
# 2025/07/12
fruit=nameless

case ${fruit} in
    "apple")
        echo "choice apple"
        ;;
    "banana")
        echo "choice banana"
        ;;
    "cherry" | "grape" | "strawberry")
        echo "cherry" or "grape" or "strawberry"
        ;;
    *)
        echo "no choice"
        ;;
esac
    
