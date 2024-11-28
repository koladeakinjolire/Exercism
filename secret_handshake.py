def commands(binary_str):
    index = len(binary_str) -1
    exponent = 0
    action_list = ['wink', 'double blink', 'close your eyes', 'jump', 'reverse actions']
    number_list = [1,2,4,8,16]
    action_dict = dict(zip(number_list, action_list))
    result_list = []
    while index >= 0 and exponent < 6:
        number = int(binary_str[index])
        result = number * (2 ** exponent)
        if result in number_list:
            result_list.append(action_dict[result])
        index -= 1
        exponent += 1
    if 'reverse actions' in result_list:
        result_list.pop(-1)
        result_list.reverse()
        
    return result_list