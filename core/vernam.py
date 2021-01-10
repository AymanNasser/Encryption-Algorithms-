from cipher import Cipher
import re

class Vernam(Cipher):
    def __init__(self, key):
        self.key = key.upper()
    
    def encrpyt(self, plain_text):
        cipher_text = ""
        regex = re.compile('[^a-zA-Z]')
        plain_text =  regex.sub('', plain_text).upper()
        
        if len(plain_text) != len(self.key):
            raise ValueError("Lengths aren't matching")
        
        for i in range(len(plain_text)):
            # print(ord(plain_text[i]),  ord(self.key[i]))
            cipher_text += chr( ord(plain_text[i]) ^ ord(self.key[i]) )

        return cipher_text
    
    def decrypt(self, cipher_text):
        pass