def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError('Number of input columns is not a multiple of three')

    digit_patterns = {
        (" _ ","| |","|_|","   "):'0',
        ("   ","  |","  |","   "): '1',
        (" _ "," _|","|_ ","   "): '2',
        (" _ "," _|"," _|","   "): '3',
        ("   ","|_|","  |","   "): '4',
        (" _ ","|_ "," _|","   "): '5',
        (" _ ","|_ ","|_|","   "): '6',
        (" _ ","  |", "  |","   "): '7',
        (" _ ","|_|", "|_|","   "): '8',
        (" _ ","|_|"," _|","   "): '9'
     }
    result = []
    for i in range(0, len(input_grid), 4):
        group = input_grid[i:i+4]
        digits = []
        for j in range(0, len(group[0]), 3):
            digit_lines = tuple(line[j:j+3] for line in group)
            digit = digit_patterns.get(digit_lines, '?')
            digits.append(digit)
        result.append(''.join(digits))
    return ','.join(result)