import re
def abbreviate(words):
    result_list = re.split(r'[_-\s]', words)
    result  = ''.join([word[0].upper() for word in result_list])
    return result




