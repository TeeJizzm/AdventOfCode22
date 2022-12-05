# Reads a text input and returns separated values
# Returns a list of lists

###########################

def toLists(filepath, group="\n", item=","):
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data
        
        # Split data into groups as list
        groups = text.split(str(group))
        
        # Split each group into parts as list of lists
        list = [items.split(str(item)) for items in groups]
        
        # return list of lists
        return list
        
########### EOF ############