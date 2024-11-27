def value(colors):
    color_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    number_list = [number for number in range(0, 10)]
    color_dict = dict(zip(color_list, number_list))
    result_list = []
    for c in colors:
        if len(colors) > 2:
            colors.pop(2)
            result_list.append(str(color_dict[c]))
        else:
            result_list.append(str(color_dict[c]))
            
    result = ''.join(result_list)
    return int(result)


