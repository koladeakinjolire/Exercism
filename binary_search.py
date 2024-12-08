def find(search_list, value):
    search_list = sorted(search_list)
    low = 0
    high = len(search_list) - 1
    while low <= high:
        middle_index = (low + high) // 2
        if search_list[middle_index] == value:
            return middle_index
        elif search_list[middle_index] < value:
            low = middle_index + 1 # checks every item after middle index
        else:
            high = middle_index - 1 #checks every item before the middle index

    raise ValueError("value noy in array")

print(find([1,3,6,3,7,9,12,31,21,4,5],12))