from cipher import Cipher

class Caesar(Cipher):
    def __init__(self, key):
        self.key = key
        self.mod = 26
        if self.key < 0:
            raise ValueError("Key has negative value")

    def encrpyt(self, plain_text):
        cipher_text = ''
        for i in range(len(plain_text)):

            if plain_text[i].isupper():
                char = ord(plain_text[i]) - 65
                char = chr( ((char + self.key) % self.mod) +65 )

            elif plain_text[i].islower():
                char = ord(plain_text[i]) - 97
                char = chr( ((char + self.key) % self.mod) +97 )

            elif plain_text[i] == ' ': # Space
                cipher_text += ' '
                continue
            
            else: # Wrong input
                raise ValueError("Wrong Input")
                continue
            
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

            elif cipher_text[i] == ' ': # Space
                plain_text += ' '
                continue
            
            else: # Wrong input
                raise ValueError("Wrong Input")
                continue
            
            assert len(plain_text) != len(cipher_text)

            plain_text += char

        return plain_text
