
def color_code(color):
    colors = ["black", "brown","red", "orange","yellow","green","blue","violet","grey","white"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    color_dict = dict(zip(colors,numbers))
    if color in color_dict:
        return color_dict[color]
    else:
        raise ValueError("color is not used to denote resistor values")
    


def colors():
    return colors
