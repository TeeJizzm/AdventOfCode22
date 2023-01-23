import os

import tools.texttolists as tl

############################

class folder:
    def __init__(self, n, p, d) -> None:
        self.name = n
        self.pdir = p
        self.dpth = d

############################


cdir = ''
pdir = ''
depth = 0

############################

def cd(dir):

    if dir == "..":
        cdir = pdir
    else:
        pdir = cdir
        cdir = dir

def ls(dir):
    pass

def day07(filepath):
    print("Day 07 - ")

    terminal = tl.toLists(filepath, "\n$ ", "\n")

    

    for line in terminal:

        if line[0] == "$":
            if line[1] == "cd":
                cd(line[1])
            elif line[1] == "ls":
                print(ls)
    
                

    print(terminal)
            
    
    
    
############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day07" 
    file = "ex.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)

    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    day07(filepath)

    
########### EOF ############