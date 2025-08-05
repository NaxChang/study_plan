#!/bin/bash
# color.sh -> filename


color () {
a="$1"
f="$2"
b="$3"
shift 3
t="$*"
echo -e "\033[${a};${f};${b}m${t}\033[0m"
}

color "$@"




# $echo -e "\033[5;35;47mHello_pink\033[0m"
