SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    if len(list_one) == 0 and len(list_two) == 0:
        return EQUAL
        
    if list_one == list_two:
        return EQUAL
        
    if not list_one:
        return SUBLIST
        
    if not list_two:
        return SUPERLIST
        
    if len(list_one) < len(list_two):
        for i in range(len(list_two) - len(list_one) + 1):
            if list_two[i:i+len(list_one)] == list_one:
                return SUBLIST
                
    if len(list_two) < len(list_one):
        for i in range(len(list_one) - len(list_two) + 1):
            if list_one[i:i+len(list_two)] == list_two:
                return SUPERLIST

    return UNEQUAL