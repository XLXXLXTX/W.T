#!/bin/bash

# check number of params to run the scripts
if [ $# -ne 2 ]
then
    echo "Usage: $0 <folder> <zip-name>"
    exit 1
fi

# check if folder exists
if ! [ -d "${1}" ]
then
    echo "Unknown folder: $1"
    exit 1
fi

# check if zip is installed
if ! which zip > /dev/null 
then
    echo "can't find zip command"
    exit 1
fi

# ensure to cd into the folder  
cd "${1}" || exit 1

# execute zip command
# use find command to include subdirectories and their content
# to make sure the files from that folder
# are added
# -@ to read the output from find 
if find . -mindepth 1 -type f | zip -r "${2}.zip" -@
then
    echo "Zip created successfully"
else
    echo "Error creating zip"
    exit 1
fi
