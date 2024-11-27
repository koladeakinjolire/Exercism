def is_valid(isbn):
    isbn_list = []
    index = 10
    position = 0
    if len(isbn) < 10:
        return False
    if isbn[-1] == "X":
        isbn_list.append(10)
    elif isbn[-1].isdigit():
        isbn_list.insert(-1, int(isbn[-1]))
    else:
        return False
    for character in isbn:
        if "-" not in isbn and len(isbn) > 10:
            return False
        if (position < 9 and index > 1) and character.isdigit():
            isbn_list.insert(position, int(character)*index)
            position += 1
            index -= 1
    return sum(isbn_list) % 11 == 0


print(is_valid("3-598-P1581-X"))
print(is_valid("3-598-21507-A"))
print(is_valid("3-598-21508-9"))
print(is_valid("3-598-21508-8"))
print(is_valid("3-598-2X507-9"))
print(is_valid("3598215088"))
print(is_valid("359821507"))
print(is_valid("3-598-21507"))
print(is_valid("3132P34035"))
print(is_valid("3-598-21507-X"))
print(is_valid("4-598-21507-B"))
print(is_valid("359821507X"))
print(is_valid("3598215078X"))
print(is_valid("00"))
print(is_valid("3-598-21515-X"))
print(is_valid(""))
print(is_valid("134456729"))
print(is_valid("3598P215088"))
print(is_valid("98245726788"))