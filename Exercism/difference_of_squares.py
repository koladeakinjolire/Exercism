def square_of_sum(number):
    number_list = [number for number in range(1, number+1)]
    total = sum(number_list)
    return total ** 2
    
def sum_of_squares(number):
    number_list = [number for number in range(1,number+1)]
    squares_list = map(lambda x: x**2, number_list)
    return sum(squares_list)


def difference_of_squares(number):
    number_list = [number for number in range(1, number+1)]
    total = sum(number_list)
    square_of_sum =  total ** 2
    squares_list = map(lambda x: x**2, number_list)
    sum_of_squares =  sum(squares_list)
    return square_of_sum - sum_of_squares
