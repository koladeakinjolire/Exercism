import re
def count_words(sentence):
    if not isinstance(sentence, str):
        raise TypeError('sentence must be a string.')
    result_dict = {}
    sentence_list = re.split(r'\s+|[-_=@#%$^&*(),.:;?!]+', sentence)
    for word in sentence_list:
        word = word.lower().strip("'")
        if not word:
            continue
        result_dict[word] = result_dict.get(word,0) + 1

    return result_dict