def rows(letter):
    if not letter.isalpha() or len(letter) != 1:
        raise ValueError('Input must be an alphabet')

    size = ord(letter) - ord('A')
    diamond_rows = []

    for i in range(size + 1):
        char = chr(ord('A') + i)
        inside_space = 2 * i - 1
        outside_space = size - i if size > 0 else 0
        if i == 0:
           row = (' ' * outside_space) + char + (' ' * outside_space)
        else:
            row = (' ' * outside_space) + char + (' ' * inside_space) + char + (' ' * outside_space)

        diamond_rows.append(row)
    diamond_rows.extend(reversed(diamond_rows[:-1]))

    return list(diamond_rows)

print(rows('K'))