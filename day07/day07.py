import os
from collections import defaultdict

import tools.texttolists as tl

############################

############################

def day07(text):
    print("Day 07 - No Space Left On Device")

    lines = tl.to2dLists(text, "\n", " ")

    dir_sizes = defaultdict(int)
    current_path = []

    for line in lines:

        # Is this line a command
        if line[0] == "$" and line[1] == "cd":
            # Change directory options
                if line[2] == "/":
                    current_path.clear()
                    current_path.append("/")
                elif line[2] == "..":
                    current_path.pop()
                else:
                    # Add new dir to path
                    current_path.append(line[2])

        elif line[0] == "dir" or line[-1] == "ls":
            pass
        # Else: Listing a file in form [ value, name ]
        else:
            if line[0].isdigit():
                size = int(line[0])
                
                for i in range(len(current_path)):
                    dir = '/'.join(current_path[:i+1]).replace("//","/")
                    dir_sizes[dir] += size

    part1 = sum(n for n in dir_sizes.values() if n <= 100000)

    for size in sorted(dir_sizes.values()):
        if size > 30000000 - (70000000 - dir_sizes["/"]):
            part2 = size
            break
    
    print("Part 1:", part1)
    print("Part 2:", part2)
    
    
############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day07/inc" 
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)

    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    day07(text)

    
########### EOF ############