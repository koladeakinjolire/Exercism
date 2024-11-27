def resistor_label(colors):
    color_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    color_dict = dict(zip(color_list,numbers))
    tolerance_colors = ["grey","violet","blue","green","brown","red","gold","silver"]
    tolerance_percentage = ["±0.05%","±0.1%","±0.25%","±0.5%","±1%","±2%","±5%","±10%"]
    tolerance_dict = dict(zip(tolerance_colors,tolerance_percentage))
    resistance = ""
    result = ""
    if len(colors) == 1:
         color = colors[0]
         resistance = str(color_dict[color]) + " ohms"
    if len(colors) == 3:
        resistance_colors = [colors[0], colors[1]]
        exponent = color_dict[colors[2]]
        for c in resistance_colors:
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
    if len(colors) == 4:
        resistance_colors = [colors[0], colors[1]]
        exponent = color_dict[colors[2]]
        tolerance = colors[3]
        for color in resistance_colors:
            result += str(color_dict[color])

        first_two = int(result)
        product = int(first_two * (10 ** exponent))

        if product < 1000:
            resistance += str(product) + " ohms"
        elif product >= 1000 and product < 1000000:
            if product % 1000 == 0:
                resistance = str(int(product/1000)) + " kiloohms"
            else:
                resistance = str(float(product/1000)) + " kiloohms"
        elif product >= 1000000 and product < 1000000000:
            resistance = str(int(product/1000000)) + " megaohms"
        else:
            resistance = str(int(product/1000000000)) + " gigaohms"
            
        if tolerance in tolerance_colors:
            resistance = resistance + " " + tolerance_dict[tolerance]
        else:
            resistance = resistance
    if len(colors) == 5:
        resistance_colors = [colors[0], colors[1], colors[2]]
        multiplier = color_dict[colors[3]]
        tolerance = colors[4]
        for c in resistance_colors:
            result += str(color_dict[c])
        
        first_three = int(result)
        product = int(first_three * (10 ** multiplier))

        if product < 1000:
            resistance += str(product) + " ohms"
        elif product >= 1000 and product < 1000000:
            resistance = str((product/1000)) + " kiloohms"
        elif product >= 1000000 and product < 1000000000:
            resistance = str((product/1000000)) + " megaohms"
        else:
            resistance = str((product/1000000000)) + " gigaohms"
            
        if tolerance in tolerance_colors:
            resistance = resistance + " " + tolerance_dict[tolerance]
        else:
            resistance = resistance

    return resistance

print(resistor_label(["orange", "orange", "black", "red"]))
print(resistor_label(["red", "black", "red", "green"]))
print(resistor_label(["green", "brown", "orange", "grey"]))
print(resistor_label(['black']))
print(resistor_label(["orange", "orange", "yellow", "black", "brown"]))
print(resistor_label(["blue", "grey", "white", "brown", "brown"]))
print(resistor_label(["violet", "orange", "red", "grey"]))
