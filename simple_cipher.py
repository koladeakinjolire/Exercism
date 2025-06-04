import random
import string 
class Cipher:
    
    k = [i for i in range(26)]
    v = list(string.ascii_lowercase)
    dict1 = dict(zip(k,v))
    dict2 = dict(zip(v,k))
    
    def __init__(self, key=None):
        self.key = key.lower() if key else self._generate_random_key()

    def _generate_random_key(self):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
        text = text.lower()
        if not all(c.isalpha() for c in text):
            return "Error: key is an invalid type (contains non-letter characters)."
            
        encoded = []
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]

            new_pos = (Cipher.dict2[char] + Cipher.dict2[key_char]) % 26
            encoded.append(Cipher.dict1[new_pos])
            
        return "".join(encoded)
        
    def decode(self, text):
        text = text.lower()
        if not all(c.isalpha() for c in text):
            return "Error: key is an invalid type (contains non-letter characters)."

        decoded = []
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]

            original_pos = (Cipher.dict2[char] - Cipher.dict2[key_char]) % 26
            decoded.append(Cipher.dict1[original_pos])

        return "".join(decoded)
