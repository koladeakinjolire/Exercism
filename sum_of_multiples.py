def sum_of_multiples(limit, multiples):
    range_list = [num for num in range(1, limit)]
    result_list = []
    for multiple in multiples:
        for number in range_list:
            product = multiple * number
            if product < limit:
                result_list.append(product)
    result_list = set(result_list)
    total = sum(result_list)
    return total

print(sum_of_multiples(98, [3, 5]))