import os

import tools.texttolists as tl

############################

def day05(filepath):
    print("Day 5 - Supply Stacks")

    data = tl.toLists(filepath, "\n\n", "\n")
    print(data)

    with open(filepath, "r") as file:
        crates, instructions = file.read().split("\n\n")
        print(crates.split("\n"))

############################

if __name__ == "__main__":
    # Change file
    #######
    day = "day05"
    file = "example.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day05(filepath)
    
########### EOF ############