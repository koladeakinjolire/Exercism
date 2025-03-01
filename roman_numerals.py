def roman(number):
    """
    Converts an integer to its Roman numeral representation.
    
    Args:
        number: An integer between 1 and 3999 (inclusive).
    
    Returns:
        str: The Roman numeral representation of the input number.
    
    Raises:
        ValueError: If number is not an integer, is less than 1, or exceeds 3999.
    """
    roman_dictionary = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC',50:'L',40:'XL',10:'X',9:'IX', 5:'V', 4:'IV',1:'I'}
    sorted_keys = sorted(roman_dictionary.keys(), reverse=True)
    if not isinstance(number, int):
        raise ValueError('number must be an integer')
    if number < 1 or number >3999:
        raise ValueError('number must be and integer between 0 and less than 4000')
    result = ""
    while number > 0:
        for key in sorted_keys:
            if number >= key:
                result += roman_dictionary[key]
                number -= key
                break
                
    return result

print(roman(1))
print(roman(3)) 
print(roman(4)) 
print(roman(435)) 
print(roman(3976))
print(roman(2984))
print(roman(1746))