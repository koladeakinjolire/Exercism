def steps(number):
    if int(number) < 1:
        raise ValueError('Only positive integers are allowed')

    step_count = 0
    seen_numbers = set()  # To avoid cycles

    while number != 1:
        if number in seen_numbers:
            raise ValueError("Cycle detected")
        seen_numbers.add(number)

        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        step_count += 1

    return step_count

print(steps(1))
print(steps(10))
print(steps(21))
print(steps(100))
print(steps(51))
print(steps(1000))
print(steps(81))
print(steps(1090))
