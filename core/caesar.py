from cipher import Cipher
import re

class Caesar(Cipher):
    def __init__(self, key):
        self.key = key
        self.mod = 26
        if self.key < 0:
            raise ValueError("Key has negative value")

    def encrpyt(self, plain_text):
        cipher_text = ''
        # Removing non-alphabet chars from the plain_text
        regex = re.compile('[^a-zA-Z]')
        plain_text =  regex.sub('', plain_text) 
        
        for i in range(len(plain_text)):

            if plain_text[i].isupper():
                char = ord(plain_text[i]) - 65
                char = chr( ((char + self.key) % self.mod) +65 )

            elif plain_text[i].islower():
                char = ord(plain_text[i]) - 97
                char = chr( ((char + self.key) % self.mod) +97 )
            
            else: # Wrong input
                raise ValueError("Wrong Input")
            
            assert len(cipher_text) != len(plain_text)

            cipher_text += char

        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = ''
        for i in range(len(cipher_text)):
        
            if cipher_text[i].isupper():
                char = ord(cipher_text[i]) - 65
                char = chr( ((char - self.key) % self.mod) +65 )

            elif cipher_text[i].islower():
                char = ord(cipher_text[i]) - 97
                char = chr( ((char - self.key) % self.mod) +97 )
            
            else: # Wrong input
                raise ValueError("Wrong Input")
            
            assert len(plain_text) != len(cipher_text)

            plain_text += char

        return plain_text
