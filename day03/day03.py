import os

#######
day = "day03"
file = "example.txt"
#######

# Get absolute filepath of file
cwd = os.getcwd()
filepath = os.path.join(cwd, day, file)

with open(filepath) as file:

    rucksacks = file.read().splitlines()

    for rucksack in rucksacks:
        
        print(len(rucksack))

        half1 = rucksack[0:len(rucksack)//2]
        half2 = rucksack[len(rucksack)//2:len(rucksack)]
        
        print (rucksack)
        print(half1, half2)
