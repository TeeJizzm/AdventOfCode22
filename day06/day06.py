## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 06

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def day06(text):
    print("Day 06 - *NAME*")
    
    part1, part2 = text, ''
    
    
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day06/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    #file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day06(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############