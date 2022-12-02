# Calculates the sum of the X largest values in a given list
# X=1 by default, returns largest value in the list

###########################

def sumTopList(list, X=1):
    
    list.sort(reverse=True) # Sort list largest to smallest
    
    # Sums X number of largest values and returns
    return sum([list[x] for x in range(X)])

########### EOF ############