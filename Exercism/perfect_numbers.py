def classify(number):
    if number < 1:
        raise ValueError ("Classification is only possible for positive integers.")
    factor_list = [num for num in range(1, number) if number % num == 0]
    total = sum(factor_list)
    if number == total:
        return "perfect"
    elif number < total:
        return "abundant"
    else:
        return "deficient"