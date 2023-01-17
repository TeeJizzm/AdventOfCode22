#!/bin/bash

for N in {01..25}
do
    #echo "Day $N"
    mkdir -p day$N
    touch day$N/{day$N.md,ex.txt,in.txt}
done

echo "Created $N folders"