import operator
def answer(question):
    #removing punctuation and splitting the string into a list for editing.
    question = question.replace('?', '').strip().split()

    #removing what, is and by
    adios_words = ['What','is','by']
    question = [word for word in question if word not in adios_words]
    
    #checking if empty or no digits
    if not question or not any(word.lstrip('-').isdigit() for word in question):
        return 'syntax error'
    
    #converting digits to integers
    question = [int(word) if word.lstrip('-').isdigit() else word for word in question]

    #mapping operators
    op_map = {
        'plus':operator.add,
        'minus':operator.sub,
        'multiplied':operator.mul,
        'divided':operator.truediv
    }
    question = [op_map[word] if word in op_map else word for word in question]


    #checking for unknown operations
    for word in question:
        if isinstance(word, str) and word not in op_map:
            return 'unknown operation'
            
    #validating structure
    for i in range(len(question)):
        if i % 2 == 0 and not isinstance(question[i], int):
            return 'syntax error'
        if i % 2 == 1 and not callable(question[i]):
            return 'syntax error'
    
    if len(question) >= 2 and len(question) < 3:
        return 'syntax error'
    
    #calculating result
    result = question[0]
    for i in range(1, len(question), 2):
        op = question[i]
        next_num = question[i+1]
        try:
            result = op(result,next_num)
        except ZeroDivisionError:
            return 'division by zero'
        
    return int(result)
        
    

question0 = "What is 2 multiplied by -2 multiplied by 3?"
print(answer(question0))
question1 = "What is 1 plus 5 minus -2?"
print(answer(question1))
question2 = "What is 33 divided by -3?"
print(answer(question2))
question3 = "What is 53 plus 2?"
print(answer(question3))
question4 = 'What is 2?'
print(answer(question4))
question5 = 'Who was the first president of the United States?'
print(answer(question5))
question6 = 'What is 1 1 plus minus 2 4?'
print(answer(question6))
question7 = 'What is -76 multiplied by -382?'
print(answer(question7))
question8 = 'What is -39 divided by 3?'
print(answer(question8))
question9 = "What is 1 plus plus 2?"
print(answer(question9))
question10 = 'What is ?'
print(answer(question10))
question11 = 'What is 52 cubed?'
print(answer(question11))