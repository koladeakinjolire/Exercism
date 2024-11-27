def convert(number):
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0 :
        return "PlingPlangPlong"
    elif number %  5 == 0 and number % 7 == 0:
        return "PlangPlong"
    elif number % 3 == 0 and number %  7 == 0 :
        return "PlingPlong"
    elif number % 7 == 0:
        return "Plong"
    elif number %  3 == 0 and number % 5 == 0:
        return "PlingPlang"
    elif number %  5 == 0:
        return "Plang"
    elif number % 3 == 0:
        return "Pling"
    else:
        return f"{number}"
    
print(convert(1))
print(convert(3))
print(convert(5))
print(convert(6))
print(convert(8))
print(convert(9))
print(convert(10))
print(convert(15))
print(convert(25))
print(convert(27))
print(convert(35))
print(convert(52))
print(convert(105))
print(convert(3125))
print(convert(7))
print(convert(14))
print(convert(21))
print(convert(49))