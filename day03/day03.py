import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'tools'))

# Index + 1 for priority of a character
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def day03(filepath):
    print("Day 3 - Rucksack Reorganization")
    
    # Get list of rucksack contents
    with open(filepath) as file:
        rucksacks = file.read().splitlines()
        
    items_in_both = []
    
    ## Part 1 ##
    # For each rucksack
    for rucksack in rucksacks:
        
        # Split rucksack into halves
        part1 = rucksack[0:len(rucksack)//2]
        part2 = rucksack[len(rucksack)//2:len(rucksack)]
        
        # Compare strings, find common items
        items_in_both.extend(set([character for character in part1 if part2.__contains__(character)]))
    
    # Sum of priorities of common items
    priorityTotal = sum((priority.index(str(char)) + 1) for char in items_in_both)
    print("Part 1: ", priorityTotal)
    
    ## Part 2 ##
    
    items_in_group = []
    # For each 3 rucksacks in a group
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        items_in_group.extend(set(c for c in group[0] if group[1].__contains__(c) and group[2].__contains__(c)))
    
    groupTotal = sum((priority.index(str(char)) + 1) for char in items_in_group)
    print("Part 2: ", groupTotal)
        
############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day03"
    file = "input.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day03(filepath)

    
########### EOF ############