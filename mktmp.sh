#!/bin/bash
# mktmp.sh

pid=$$
echo "${pid}"

tmp_dir=$(mktemp -d -t ci-$(date +%Y%m%d%H%M%S)-XXXXXXXXXXX)

echo "${tmp_dir}"

cleanup () {
    echo "remove tmp"
    rm -fr "${tmp_dir}"
    echo "clean up"
    exit
}

trap cleanup SIGINT SIGTERM

generate_files () {
    local i=1
    while true; do
        echo "$date" > "${tmp_dir}/file${i}.txt"
        i=$((i+1))
        sleep 1
    done
}

generate_files