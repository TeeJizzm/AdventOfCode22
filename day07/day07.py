import os

import tools.texttolists as tl

############################

def day07(filepath):
    print("Day 07 - ")
    
    
    
############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day07" 
    file = "example.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day07(filepath)

    
########### EOF ############