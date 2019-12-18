#!/bin/bash

#set -x  # Debug output.
set -e  # Terminate the script upon error.

FILES="$(ls *.service)"  # Get a list of all *.service files.

for file in $FILES
do
    cp $file /etc/systemd/system/
    systemctl enable $file 2>&1 > /dev/null
    systemctl start $file 2>&1 > /dev/null
    echo Installed $file
done
