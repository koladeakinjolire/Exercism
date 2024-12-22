def append(list1, list2):
    list1 +=  list2
    return list1

def concat(lists):
    result = []
    for lst in lists:
        result += lst
    return result
        
def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result

def length(list):
    return len(list)

def map(function, list):
    result = [function(item) for item in list]
    return result

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial
    
def reverse(list):
    result = list[::-1]
    return result