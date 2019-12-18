#!/bin/bash

#set -x  # Debug output.
set -e  # Terminate the script upon error.

FILES="$(ls *.service)"  # Get a list of all *.service files.

for file in $FILES
do
    systemctl stop $file 2>&1 > /dev/null
    systemctl disable $file 2>&1 > /dev/null
    rm -rf /etc/systemd/system/$file
    echo Removed $file
done
