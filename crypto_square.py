import math
import numpy as np
def cipher_text(plain_text):
    #removing any whitespaces
    text = "".join(char.lower() for char in plain_text if char.isalpha())
    text_len = len(text)
    #edge cases
    if text_len < 1:
        return ""
    if text_len == 1:
        return text
    
    root_len = text_len ** 0.5
    text_list = list(text)
    
    #defining row, column, product and difference values
    c = math.ceil(root_len) #columns
    r = math.floor(root_len) #rows

    if c * r < text_len:
        r = c

    product = c * r
    diff = product - text_len

    #appending spaces at the end of the text, if the length of the text is not a perfect square
    for _ in range(diff):
        text_list.append(" ")
    
    #creating a list of rows
    result_list = []
    for i in range(r):
        row_start = i * c
        row_end = row_start + c
        result_list.append(text_list[row_start:row_end])

    #transposing the rows to columns
    transposed_list = np.transpose(result_list).tolist()

    #joining the columns to form the final cipher text
    for i in range(len(transposed_list)):
        transposed_list[i] = "".join(transposed_list[i])
    
    #joining the result list to form the final string
    result = " ".join(transposed_list)
    return result

value1 = "Where did you find this? This is incredibly fun! i hope we get to do it again @ some point."
value2 = "be"
value3 = "tiger"
value4 = "cats"
value5 = "monkey"
value6 = "This is amazing!"
value7 = "Chill out."
value8 = "If man was meant to stay on the ground, god would have given us roots."
value9 = "Is this a test? Yes, it is a test."
value10 = "a0b1pbo23dce4m56f7lgk89h@#$%^h&n*."

print(cipher_text(value1))
print(cipher_text(value2))
print(cipher_text(value3))
print(cipher_text(value4))
print(cipher_text(value5))
print(cipher_text(value6))
print(cipher_text(value7))
print(cipher_text(value8))
print(cipher_text(value9))
print(cipher_text(value10))