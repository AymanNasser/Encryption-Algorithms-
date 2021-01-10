from cipher import Cipher
import numpy as np
from textwrap import wrap
import re

class Hill(Cipher):
    def __init__(self, key_mat, filler_letter='X'):
        self.key_mat = np.array(key_mat)
        self.mat_size = len(self.key_mat[0])
        self.filler = filler_letter
        self.mod = 26

    def encrpyt(self, plain_text):
        cipher_text = ""
        # Removing any non alphabet from the plain_text
        regex = re.compile('[^a-zA-Z]')
        plain_text =  regex.sub('', plain_text).upper()
        plain_text = wrap(plain_text, self.mat_size)

        # Fill plain text length to be of equal m portions
        if len(plain_text[-1]) - self.mat_size != 0:
            plain_text[-1] += self.filler * abs(len(plain_text[-1]) - self.mat_size )
            
        for m in plain_text:
            text = []

            for letter in m:
                text.append( ord(letter) - 65)

            text = np.array(text)
            out = np.dot(self.key_mat, text) % self.mod

            for i in out:
                cipher_text += chr(i + 65) 

        return cipher_text.lower()

    def decrypt(self, cipher_text):
        pass
        