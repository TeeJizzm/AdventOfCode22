def texttolist(filepath):
    with open(filepath, "r") as file:
        
        text = file.read()
        
        data = text.split("\n\n")
        
        list = [item.split("\n") for item in data]
        
        return list
        
    