# Reads a text input and returns separated values
# Returns a list of lists

###########################

def toLists(text, group="\n", item=","):
        
    # Split data into groups as list
    groups = text.split(str(group))
        
    # Split each group into parts as list of lists
    list = [items.split(str(item)) for items in groups]
        
    # return list of lists
    return list
        
########### EOF ############