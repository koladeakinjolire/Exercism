import string
alphabet = list(string.ascii_lowercase)
cipher = alphabet[::-1]

def encode(plain_text):
    result = ''
    for char in plain_text.lower():
        if char == " " or char in string.punctuation:
            continue 
        elif char.isdigit():
            result += char
        else:
            result += cipher[alphabet.index(char)]
    
    result_with_spaces = ' '.join([result[i:i+5] for i in range(0, len(result), 5)])
            
    return result_with_spaces


def decode(ciphered_text):
    result = ""
    for char in ciphered_text.lower():
        if char == " " or char in string.punctuation:
            continue
        elif char.isdigit():
            result += char
        else:
            result+= alphabet[cipher.index(char)]
    return result