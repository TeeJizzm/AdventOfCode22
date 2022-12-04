# Reads a text input and returns separated values
# Returns a list of lists

###########################

def toLists(filepath, group="\n", part=","):
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data
        
        # Split data into groups as list
        groups = text.split(str(group))
        
        # Split each group into parts as list of lists
        list = [item.split(str(part)) for item in groups]
        
        # return list of lists
        return list
        
########### EOF ############