#!/bin/bash
###################################################
#

###################################################
# Generate folders                                #
###################################################
for N in {01..25}
do
    #echo "Day $N"
    mkdir -p day$N

    # Other files
    touch day$N/{day$N.md,ex.txt,in.txt}

    # Initiate Python file for each day from template
    sed "s/XX/$N/g" python_template > day$N/day$N.py

    # Initiate rust package - VScode will support this easily this way
    cargo new day$N/rs --quiet --vcs none

done
###################################################
echo "Created $N folders"