#!/bin/bash

destination="${1}"
command="
echo '>>>>>>>>>>>>>';
date;
ping -c 1 ${destination} | grep bytes;
echo '<<<<<<<<<<<<<';
sleep 3;
"
echo ${command}
exec ./whiletrue.sh "${command}"
