import os

from tools import texttolists as tl
from tools import sumlist as sl

############################

def day1(filepath):
    print("Day 1 - Calorie Counting")
    
    # Get a list of elves from the file
    ## \n\n to divide data into groups/elves
    ## \n to divide the groups into items/calories
    elves = tl.toLists(filepath, "\n\n", "\n")
    
    calories = [] # empty list
    
    # Calculate total calories carried by each elf
    for elf in elves:
        calorie = [int(item) for item in elf] # Convert each elf's item's calories to integer
        calories.append(sum(calorie)) # Calculate total calories carried per elf
    
    part1 = sl.sumTopList(calories) # calculate answer to part 1
    part2 = sl.sumTopList(calories, 3) # calculate answer to part 2
    
    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day01"
    file = "input1.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)

    day1(filepath)
    
########### EOF ############