def is_armstrong_number(number):
    number = str(number)
    exponent = len(number)
    total_list = [int(digit) ** exponent for digit in number]
    total = sum(total_list)
    if total == int(number):
        return True
    return False 

print(is_armstrong_number(153))
print(is_armstrong_number(175))