def factors(value):
    factor_list = []
    i = 2  
    
    while i * i <= value:  
        while value % i == 0:
            factor_list.append(i)
            value //= i  
        i += 1  

    if value > 1:  
        factor_list.append(value)
    
    return factor_list
