def egg_count(display_value):
    if display_value == 0:
        return 0
        
    binary_list = []
    while display_value >= 1:
        value = display_value % 2
        binary_list.append(value)
        display_value //= 2
        
    return binary_list.count(1)