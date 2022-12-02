# Reads a text input and returns separated values
# Returns a list of lists

###########################

def textto2d(filepath):
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        # Read data
        text = file.read()
        
        # Divide data into groups
        data = text.split("\n\n")
        
        # Divide groups into items
        list = [item.split("\n") for item in data]
        
        # return list of lists
        return list
        
########### EOF ############