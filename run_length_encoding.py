string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
encoded_string = '12W1B12W3B24W1B'
def decode(encoded_string):
    result = []
    num = 0
    for char in encoded_string:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            count = num if num > 0 else 1
            result.append(char*count)
            num = 0
    return "".join(result)
def encode(string):
    if not string:
        return ""
    result = []
    count = 1
    current_char = string[0]
    for char in string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
            
    result.append(str(count) + current_char )
    return "".join(result)

print(decode(encoded_string))
print(encode(string))