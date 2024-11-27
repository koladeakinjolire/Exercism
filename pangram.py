import string 
def is_pangram(sentence):
    sentence_set = set(sentence.lower())
    alphabet_set = set(string.ascii_lowercase)
    if alphabet_set.issubset(sentence_set):
        return True
    else:
        return False
    
print(is_pangram(""))
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))
print(is_pangram("five boxing wizards jump quickly at it"))
