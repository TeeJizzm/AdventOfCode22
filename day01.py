import os

from tools import textlist as tl
from tools import sumlist as sl

############################

def day1():
    
    # Change file
    ####### 
    file = "input1.txt"
    #######
    
    # Get absolute filepath of file
    cwd = os.getcwd()
    filepath = os.path.join(cwd, day, file)
    
    # Get a list of elves from the file
    elves = tl.textto2d(filepath)
    
    calories = [] # empty list
    
    # Calculate total calories carried by each elf
    for elf in elves:
        calorie = [int(item) for item in elf] # Convert each elf's item's calories to integer
        calories.append(sum(calorie)) # Calculate total calories carried per elf
    
    part1 = sl.sumtoplist(calories) # calculate answer to part 1
    part2 = sl.sumtoplist(calories, 3) # calculate answer to part 2
    
    print("Answer to Part 1: ", part1)
    print("Answer to Part 2: ", part2)
    
############################

if __name__ == "__main__":
    day = "day01"
    day1()
    
########### EOF ############