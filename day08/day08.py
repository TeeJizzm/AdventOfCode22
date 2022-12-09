import os

import tools.texttolists as tl

############################

def day08(filepath):
    print("Day 08 - Treetop Tree House")
    
    tl.toLists(filepath)


############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day08" 
    file = "example.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day08(filepath)

    
########### EOF ############