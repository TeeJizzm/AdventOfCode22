import os
import numpy as np

import tools.texttolists as tl

############################

def isVisible(trees, x, y):

    #print(" # ", trees[:x, y], trees[x, y], trees[x+1:, y])

    if seesEdge(trees[x, y], trees[x, :y]) is True:
        return 1
    if seesEdge(trees[x, y], trees[x, y+1:]) is True:
        return 1
    if seesEdge(trees[x, y], trees[:x, y]) is True:
        return 1
    if seesEdge(trees[x, y], trees[x+1:, y]) is True:
        return 1
    
    return 0

def isScenic(trees, x, y):

    #print(" # ", trees[:x, y], trees[x, y], trees[x+1:, y])

    return (seesTrees(trees[x, y], (trees[x, y-1::-1])) *
            seesTrees(trees[x, y], trees[x, y+1:]) *
            seesTrees(trees[x, y], (trees[x-1::-1, y])) *
            seesTrees(trees[x, y], trees[x+1:, y])
            )
    

def seesEdge(tree, row):
    if tree > max(row):
        return True
    else:
        return False

def seesTrees(tree, row):
    # Return number of trees until view is blocked
    if tree > max(row): # Return number of trees seen
        return len(row)
    else: # Return first index of blocking tree
        return (np.where(tree <= row)[0][0]+1)


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

    # Variable for part 2
    scenicScore = []

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            visibleTrees += isVisible(trees, x, y)
            scenicScore.append(isScenic(trees, x, y))

    ## Results
    print("Part 1: ", visibleTrees)
    print("Part 2: ", max(scenicScore))

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