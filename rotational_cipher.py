import string
def rotate(text, key):
    alphabet = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    if not isinstance(text, str):
        raise TypeError("Text must be in string format")
    
    if key < 0 or key > 26:
        raise ValueError("Key must be between 0 and 25")

    if key == 0 or key == 26:
        return text
    
    result = ""
    for char in text:

        if char.isalpha() and char.isupper():
            index = alphabet_upper.index(char)
            shifted_index = (index + key) % 26 
            result += alphabet[shifted_index].upper()
            
        elif char.isalpha() and char.islower():
            index = alphabet.index(char)
            shifted_index = (index + key) % 26
            result += alphabet[shifted_index].lower()
            
        else:
            result += char
    return result

print(rotate("The quick brown fox jumps over the lazy dogs", 20))
print(rotate("Nby kocwe vliqh zir dogjm ipyl nby futs xiam", 20))