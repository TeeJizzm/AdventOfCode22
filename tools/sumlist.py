# Calculates the sum of the X highest values in a given list
# X=1 by default, returns highest value in the list

###########################

def sumtopoflist(list, topnumbers=1):
    
    list.sort(reverse=True) # Sort list highest to lowest
    
    total = 0 # Initialise as 0
    for i in range(topnumbers): # For X highest values
        total += list[i] # Running total of highest values
    
    return total

########### EOF ############