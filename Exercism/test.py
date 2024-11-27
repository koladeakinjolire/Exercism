colors = ['brown']
color_list = ["black", "brown","red", "orange","yellow","green","blue","violet","grey","white"]
numbers = [0,1,2,3,4,5,6,7,8,9]
color_dict = dict(zip(color_list,numbers))
resistance = str(color_dict[colors[0]]) + " ohms"
print(resistance)