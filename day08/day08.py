import os
import numpy as np

import tools.texttolists as tl

############################

def isVisible(trees, x, y):

    #print(" # ", trees[:x, y], trees[x, y], trees[x+1:, y])

    if visibility(trees[x, y], trees[x, :y]):
        return 1
    if visibility(trees[x, y], trees[x, y+1:]):
        return 1
    if visibility(trees[x, y], trees[:x, y]):
        return 1
    if visibility(trees[x, y], trees[x+1:, y]):
        return 1
    
    return 0
    

def visibility(tree, row):
    #print(tree, ":", row)
    if tree > max(row):
        return True
    else:
        return False


def day08(filepath):
    print("Day 08 - Treetop Tree House")
    
    data = tl.toLists(filepath, "_", "\n")

    ## Data formatting

    forest = []

    for row in data[0]:
        # String unpack for each digit
        forest.append([*str(row)])

    trees = np.array(forest)

    rows, cols = trees.shape # Columns and Rows of forest

    # Count for visible trees, begins with each tree in the perimeter.
    visibleTrees = (rows + cols - 2) * 2 

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            visibleTrees += isVisible(trees, x, y)

    print("Part 1: ", visibleTrees)

############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day08" 
    file = "input.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day08(filepath)

    
########### EOF ############