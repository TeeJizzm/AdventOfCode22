#!/bin/bash

###################################################

THIS_PATH="$(dirname -- "${BASH_SOURCE[0]}")"
echo From $THIS_PATH


###################################################
# Generate folders                                #
###################################################
# Folder for tools

mkdir tools
cp -r $THIS_PATH/python_tools/* tools


# Folder for each day
for N in {01..25}
do
    #echo "Day $N"
    mkdir -p day$N/{src,inc}

    # Other files
    touch day$N/day$N.md
    touch day$N/inc/{ex.txt,in.txt}

    ## Python
    # Insert a Python file for each day from template
    sed "s/XX/$N/g" $THIS_PATH/python_template > day$N/day$N.py

    ## Rust
    # Initiate rust package - VScode will support this
    cargo init day$N --quiet --vcs none

done
###################################################
echo "Created $N folders"