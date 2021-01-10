from cipher import Cipher
import re

class Vigenere(Cipher):
    def __init__(self, key, mode=True):
        self.key = key.upper()
        self.mod = 26 
        # If False ==> Repeating mode, else ==> Auto mode
        self.mode = mode 

    def encrpyt(self, plain_text):
        cipher_text = ""
        # Removing any non alphabet from the plain_text
        regex = re.compile('[^a-zA-Z]')
        plain_text =  regex.sub('', plain_text).upper()

        if self.mode == True:
            key = self.key + plain_text[: (len(plain_text) - len(self.key))]
        else:
            key = self.key * int(len(plain_text) / len(self.key) + 1)
            key = key[: len(plain_text)]

        print(key)
        print(plain_text)

        for i in range(len(plain_text)):
            cipher_text += chr( (ord(plain_text[i]) + ord(key[i])) % self.mod + 65) 

        return cipher_text.lower()

    def decrypt(self, cipher_text):
        pass