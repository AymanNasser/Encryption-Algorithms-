from cipher import Cipher
import re

class Vernam(Cipher):
    def __init__(self, key):
        self.key = key.upper()
        self.mod = 26
    
    def encrpyt(self, plain_text):
        cipher_text = ""
        regex = re.compile('[^a-zA-Z]')
        plain_text =  regex.sub('', plain_text).upper()
        
        if len(plain_text) != len(self.key):
            raise ValueError("Lengths aren't matching")
        
        for i in range(len(plain_text)):
            # print(ord(plain_text[i]),  ord(self.key[i]))
            cipher_text += chr( (((ord(plain_text[i]) - 65) + (ord(self.key[i]) - 65)) % self.mod) + 65 )

        return cipher_text
    
    def decrypt(self, cipher_text):
        pass