import os
import sys

sys.path.append(os.path.join(os.getcwd(), "tools"))

from tools import texttolists as tl

############################

def isContained(L1, H1, L2, H2):
    if int(L1)-int(L2) <= 0 and int(H1)-int(H2) >= 0:
        return 1 # If pair1 contains pair2
    elif int(L2)-int(L1) <= 0 and int(H2)-int(H1) >= 0:
        return 1 # If pair2 contains pair1
    else:
        return 0

def isOverlapped(L1, H1, L2, H2):
    if int(L1) <= int(L2) <= int(H1) or int(L1) <= int(H2) <= int(H1):
        return 1 # If pair2 overlaps pair1
    elif int(L2) <= int(L1) <= int(H2) or int(L2) <= int(H1) <= int(H2):
        return 1 # If pair1 overlaps pair2
    else:
        return 0

############################

def day04(filepath):
    print("Day 4 - Camp Cleanup")
    
    # Get assignments from file
    assignments = tl.toLists(filepath, "\n", ",")
    
    contained = []
    overlaps = []
    
    # Each line is an assignment pair
    for elf1, elf2 in assignments:
        
        lower1, higher1 = elf1.split("-")
        lower2, higher2 = elf2.split("-")
        
        contained.append(isContained(lower1, higher1, lower2, higher2))
        overlaps.append(isOverlapped(lower1, higher1, lower2, higher2))

    print("Part 1: ", sum(contained))
    print("Part 2: ", sum(overlaps))
    
    
############################

if __name__ == "__main__":
    # Change file
    #######
    day = "day04"
    file = "input.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day04(filepath)
    
########### EOF ############