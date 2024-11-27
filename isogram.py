def is_isogram(string):
    new_sentence_list = []
    string = string.lower()
    for character in string:
        if character.isalpha() and character not in new_sentence_list:
            new_sentence_list.append(character)
        if not character.isalpha():
            new_sentence_list.append(character)
    return len(new_sentence_list) == len(string)