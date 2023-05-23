## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 02

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables

decrypt = {
    "A": 1, # Rock
    "X": 1,
    "B": 2, # Paper
    "Y": 2,
    "C": 3, # Scissors
    "Z": 3
}

mat_part1 = [
    [4, 8, 3], 
    [1, 5, 9],
    [7, 2, 6]
]
#    a      b      c
#[[x,y,z][x,y,z][x,y,z]]
#[[3,6,0][0,3,6][6,0,3]]

mat_part2 = [
    [3, 4, 8],
    [1, 5, 9],
    [2, 6, 7]
]
#    a      b      c
#[[0,3,6][0,3,6][0,3,6]]
#[[z,x,y][x,y,z][y,z,x]]

############################
# Functions

def day02(text):
    print("Day 02 - Rock Paper Scissors")
    
    rounds = tl.to2dLists(text, "\n", " ")
    
    part1, part2 = 0, 0
    
    for opp, player in rounds:
        
        part1 += mat_part1[decrypt[opp]-1] [decrypt[player]-1]
            
        part2 += mat_part2[decrypt[opp]-1] [decrypt[player]-1]
        
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day02/inc" 
    
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

    part1, part2 = day02(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############