#/bin/bash
# 檔名std_test.sh

if [ ! -f file.txt ]; then
    echo "Error:file does not exist." >&2
    exit 1
fi


