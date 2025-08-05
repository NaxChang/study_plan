#!/bin/bash
# file_name>-bar.sh
len_bar () {
    local num=${1}
    local s_num=$((100-num))
    str=""
    for ((i=1; i<=${num}; i++)) {
        str="${str}*"
    }
    for ((i=1; i<=${s_num}; i++)); do
        str="${str}-"
    done
    if (( ${num}>=60 )); then
        echo -e "\033[32m${num} ${str}\033[0m"
    else
        echo -e "\033[31m${num} ${str}\033[0m"
    fi
    # echo "${1} ${str}"

}

len_bar "$1"

