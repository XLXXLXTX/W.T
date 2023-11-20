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

# execute zip command
# -j to remove te folder structure and 
# add only the files from that folder
if zip -j "${1}/${2}.zip" "${1}"/* > /dev/null
then
    echo "Zip created successfully"
else
    echo "Error creating zip"
    exit 1
fi
