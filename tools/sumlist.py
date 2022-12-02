def sumtopoflist(list, topnumbers=1):
    
    list.sort(reverse=True)
    
    total = 0
    
    for i in range(topnumbers):
        total += list[i]
        
    return total
