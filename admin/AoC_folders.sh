#!/bin/bash
###################################################




###################################################
# Generate folders                                #
###################################################
for N in {01..25}
do
    #echo "Day $N"
    mkdir -p day$N

    # Other files
    touch day$N/{day$N.md,ex.txt,in.txt}

    ## Python
    # Insert a Python file for each day from template
    sed "s/XX/$N/g" python_template > day$N/day$N.py

    ## Rust
    # Initiate rust package - VScode will support this
    cargo new day$N/rs --quiet --vcs none

    ## Tools + scripts
    # Copy tools folder
    cp -R Tools 

done
###################################################
echo "Created $N folders"