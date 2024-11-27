"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    new_word = 'un'+ word
    return new_word

print(add_prefix_un('holy'))
    


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    new_string = prefix + ' :: ' + ' :: '.join(prefixed_words)
    return new_string


test_words = ('en', 'close', 'joy', 'lighten')
print(make_word_groups(test_words))

word = 'resourcefulness'
print(word[:-4])
print(word[-3])
  



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    vowels = ['a','e','i','o','u']
    new_word = word[:-4]
    if new_word[-1] in vowels:
        new_word = new_word[:-1] + 'y'
        return new_word
    
    return new_word
print(remove_suffix_ness('resourcefulness'))
print(remove_suffix_ness('happiness'))


    


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    sentence = sentence[:-1]
    words = sentence.split(' ')
    new_word = words[index] + 'en'
    return new_word

sentence = ("It got dark as the sun set.")
print(adjective_to_verb(sentence, 2))
