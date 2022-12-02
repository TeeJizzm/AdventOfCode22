# Reads a text input and returns separated values
# Returns a list of lists

###########################

def textto2d(filepath):
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data
        
        groups = text.split("\n\n") # Divide data into a list of groups by double endlines
        
        list = [item.split("\n") for item in groups] # Divide groups into lists of items
        
        # return list of lists
        return list
        
########### EOF ############