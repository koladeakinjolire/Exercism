import re
def translate(text):
    constant = 'ay'
    vowels = 'aeiou'
    
    def translate_word(word):
      
        if word[:2] in {'xr', 'yt'}:
            return word + constant
        
        
        if word[0] == 'y':
            return word[1:] + 'y' + constant
        
        
        match = re.match(r'([^aeiouy]*qu|[^aeiouy]+)', word)
        if match:
            cluster = match.group(1)
            return word[len(cluster):] + cluster + constant
        
        
        if word[0] in vowels:
            return word + constant
        
        return word  
    
    
    words = text.split()  
    translated_words = [translate_word(word) for word in words]
    return ' '.join(translated_words)  


print(translate('apple'))
print(translate('ear'))
print(translate('igloo'))
print(translate('object'))
print(translate('under'))
print(translate('yttria'))
print(translate('xray'))
print(translate('yellow'))
print(translate('dunkirk'))
print(translate('pig'))
print(translate('koala'))
print(translate('past'))
print(translate('queen'))
print(translate('square'))
print(translate('chair'))
print(translate('therapy'))
print(translate('thrush'))
print(translate('school'))
print(translate('my'))
print(translate('rhythm'))
print(translate('thyroid'))
print(translate('cryogenic'))
print(translate('quick fast run'))