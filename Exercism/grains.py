def square(number):
    if number > 64 or number < 1:
        raise ValueError ("square must be between 1 and 64")
    num_list = [n for n in range(1, 65)]
    square_dict = {}
    for num in num_list:
        if num  == 1:
            square_dict[num] = num
        else:
            square_dict[num] = 2 ** (num - 1)
    return square_dict[number]



def total():
    total_list = [ 2 ** (num - 1) for num in range(1,65)]
    return sum(total_list)
     



print(square(1))
print(square(2))
print(square(3))
print(square(4))
print(square(5))
print(square(6))
print(square(7))
print(square(8))
print(square(9))
print(square(10))
print(square(11))
print(square(12))
print(square(13))
print(square(14))
print(total())