import os
import numpy as np

from tools import textlist as tl

############################

def day1():
    file = "example1.txt"
    
    cwd = os.getcwd()
    filepath = os.path.join(cwd, day, file)
    
    list = tl.texttolist(filepath)
    
    print(list)
    

    
############################

if __name__ == "__main__":
    day = "day01"
    day1()
    
########### EOF ############