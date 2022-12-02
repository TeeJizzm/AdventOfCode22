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
    
    # Get a list of the data in the file
    elves = tl.textto2d(filepath)
    
    calories = []
    
    for elf in elves:
        calorie = [int(item) for item in elf]
        calories.append(sum(calorie))
    
    part1 = sl.sumtopoflist(calories)
    part2 = sl.sumtopoflist(calories, 3)
    
    print(part1, "\n", part2)
    

    
    
    
############################

if __name__ == "__main__":
    day = "day01"
    day1()
    
########### EOF ############