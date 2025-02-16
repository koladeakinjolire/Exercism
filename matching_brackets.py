def is_paired(input_string):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        if char in bracket_pairs.values(): 
            stack.append(char)
        elif char in bracket_pairs.keys():  
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    return not stack