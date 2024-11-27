def label(colors):
    color_list = ["black", "brown","red", "orange","yellow","green","blue","violet","grey","white"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    color_dict = dict(zip(color_list,numbers))
    colors = colors[:3]
    exponent = color_dict[colors[2]]
    result_colors = colors[:2]
    result = ""
    resistance = ""
    for c in result_colors:
        result += str(color_dict[c])
    first_two = int(result)
    product = int(first_two * (10 ** exponent))
    if product < 1000:
        resistance += str(product) + " ohms"
    elif product >= 1000 and product < 1000000:
        resistance = str(int(product/1000)) + " kiloohms"
    elif product >= 1000000 and product < 1000000000:
        resistance = str(int(product/1000000)) + " megaohms"
    else:
        resistance = str(int(product/1000000000)) + " gigaohms"
    return resistance

print(label(['orange','yellow','blue']))