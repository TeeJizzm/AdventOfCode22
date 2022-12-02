import os

from tools import texttolists as tl

############################

def day2(filepath):
    print("Day 2 - Rock, Paper, Scissors")

    rounds = tl.toLists(filepath, "\n", " ")

    for round in rounds:
        print("Opponent plays: ", round[0])
        print("Response plays: ", round[1])

############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day02" 
    file = "example1.txt"
    #######
    
    # Get absolute filepath of file
    cwd = os.getcwd()
    filepath = os.path.join(cwd, day, file)
    
    day2(filepath)

    
########### EOF ############