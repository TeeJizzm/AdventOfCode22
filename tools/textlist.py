def texttolist(filepath):
    with open(filepath, "r") as file:
        
        data = file.read()
        
        list = data.replace("\n", ",")
        list = list.split(",,")
        
        return list
        
    