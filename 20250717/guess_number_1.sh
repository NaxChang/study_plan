#!/bin/bash
# 檔名:guess_number_1.sh

min_n=1
max_n=100
g_num=0

t_num=$(shuf -i 1-100 -n 1)

while true; do
    read -p "input number: " g_num
    if ! [[ ${g_num} =~ ^[0-9]+$ ]]; then
        echo "invalid number"
        continue
    fi
    if [ "${g_num}" -lt "${min_n}" ] || [ "${g_num}" -gt "${max_n}" ]; then
        echo "out of range!! must be between ${min_n} and ${max_n}"
        continue
    fi
    if [ ${g_num} -lt ${t_num} ] && [ ${g_num} -gt ${min_n} ]; then
        min_n=${g_num}
        echo "too small"
    elif [ ${g_num} -gt ${t_num} ] && [ ${g_num} -lt ${max_n} ]; then
        max_n=${g_num}
        echo "too big"
    elif [ ${g_num} -eq ${t_num} ]; then
        echo "bingo"
        exit 0
    fi
    echo "current range: ${min_n} ~ ${max_n}"
done
