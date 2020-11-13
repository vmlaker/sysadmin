#!/bin/bash

set -e  # Exit upon first error.
#set -x  # Uncomment for debugging.

src_root="localhost:/mnt/g"
src_paths=(
"path1"
"path2"
"path3"
)

dst_root="data2"

log () { echo "$@"; }
run () { log "Running command: $@"; eval $@; }

for ((ii=0; ii < ${#src_paths[@]}; ii++)); do
    src_path=${src_paths[$ii]}
    full_src_path=${src_root}/${src_path}

    # Append backslash to the source path so that rsync
    # will copy *content* of the source path.
    full_src_path="${full_src_path}/"

    dst_dir=${dst_root}/${src_path}
    run "mkdir -p ${dst_dir}"
    
    command="rsync -avue 'ssh -p 50000' ${full_src_path} ${dst_dir}"
    run "${command}"

done
exit 0
