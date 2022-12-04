import os

# Index + 1 for priority of a character
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def day03(filepath):
    # Get list of rucksack contents
    with open(filepath) as file:
        rucksacks = file.read().splitlines()
        
    items_in_both = []
    
    # For each rucksack
    for rucksack in rucksacks:
        
        # Split rucksack into halves
        part1 = rucksack[0:len(rucksack)//2]
        part2 = rucksack[len(rucksack)//2:len(rucksack)]
        
        # Compare strings, find common items
        items_in_both.extend(set([character for character in part1 if part2.__contains__(character)]))
    
    ## Part 1
    # Sum of priorities of common items
    priorityTotal = sum((priority.index(str(char)) + 1) for char in items_in_both)
    print(priorityTotal)
    
        
############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day03"
    file = "input.txt"
    #######

    # Get absolute filepath of file
    cwd = os.getcwd()
    filepath = os.path.join(cwd, day, file)
    
    day03(filepath)

    
########### EOF ############