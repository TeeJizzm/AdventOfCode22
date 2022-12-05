import os

import tools.texttolists as tl

############################

def day05(filepath):
    print("Day 5 - Supply Stacks")

    crates, instructions = tl.toLists(filepath, "\n\n", "\n")
    print(crates)



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