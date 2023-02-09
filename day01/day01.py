## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 01

############################
# Imports

import os

import tools.texttolists as tl

import tools.sumlist as sl

############################
# Variables



############################
# Functions

def day01(text):
    print("Day 01 - Calorie Counting")

    elves = tl.toList(text, "\n\n")
    elves = [elf.splitlines() for elf in elves]

    calories = []

    # Calculate the total calories carried by each elf
    for elf in elves:
        
        calorie = [int(item) for item in elf]
        calories.append(sum(calorie))

        #print(calorie)
    
    part1 = sl.sumTopList(calories)
    part2 = sl.sumTopList(calories, 3)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day01/inc" 
    
    # Change file
    #######
    #file = "ex.txt"
    file = "in.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day01(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############