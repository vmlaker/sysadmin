#!/bin/bash

dpkg -l | tail +6 | grep 'ii ' | awk '{ print $2 }' | awk -F\: '{ print $1 }' | sort -u
