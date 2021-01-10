from cipher import Cipher
import re
from textwrap import wrap

class Playfair(Cipher):
    def __init__(self, keyword, filler_letter='X'):
        self.keyword = keyword.upper()
        self.filler = filler_letter
        self.mat = [[None for i in range(5)] for j in range(5)]
        self._letter_location = [None] * 26

        self.__fill_mat()
         
    # Filling the matrix with the keyword
    def __fill_mat(self):
        assert self.keyword is not None

        is_char_occurred = [0] * 26
        is_char_occurred[9] = 1 # Assuming no J
        for char in self.keyword:
            is_char_occurred[ ord(char)-65 ] = 1

        row = 0
        col = 0
        for i in range(len(self.keyword)):
            self.mat[row][col] = self.keyword[i]

            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(26 - len(self.keyword) ):
            for j in range(26):

                if is_char_occurred[j] == 0:
                    self.mat[row][col] = chr(j + 65)
                    is_char_occurred[j] = 1
                    break

            col += 1
            if col > 4:
                col = 0
                row += 1

        # Saving each char location from the matrix 
        for row in range(5):
            for col in range(5):
                self._letter_location[ ord(self.mat[row][col]) - 65] = str(row) + str(col)    


    def __preprocess_text(self, plain_text):
        # Removing spaces from the plain_text
        regex = re.compile('[^a-zA-Z]')
        plain_text =  regex.sub('', plain_text).upper()
        plain_text = plain_text.replace("J", "I") 
        # Checking if there is a duplicates in each pair
        print(plain_text)
        i = 1
        plain_text_ = []
        while i < len(plain_text):
            print(plain_text[i-1], plain_text[i])
            if plain_text[i-1] == plain_text[i]:
                plain_text_.append(plain_text[i-1] + self.filler)
                i +=1

            else:
                plain_text_.append(plain_text[i-1] + plain_text[i])
                i += 2        

        # If the last char of the original plain text not the same of plain_text_
        # therefore, we need to append the last char 
        if plain_text_[-1][-1] != plain_text[-1]:
            plain_text_.append(plain_text[-1])

        if len(plain_text_[-1]) == 1:
            plain_text_[-1] += 'X'
        print(plain_text_)
        return plain_text_

    def encrpyt(self, plain_text):
        cipher_text = ""
        plain_text = self.__preprocess_text(plain_text)
        
        for pair in plain_text:
            char_1 = str(pair)[0]
            char_2 = str(pair)[1]

            row_col_1 = self._letter_location[ord(char_1) - 65]
            row_1 = int(row_col_1[0])
            col_1 = int(row_col_1[1])

            row_col_2 = self._letter_location[ord(char_2) - 65]
            row_2 = int(row_col_2[0])
            col_2 = int(row_col_2[1])

            if col_1 == col_2:
                cipher_text += self.mat[ (row_1+1)%5 ][col_1]
                cipher_text += self.mat[ (row_2+1)%5 ][col_2]

            elif row_1 == row_2:
                cipher_text += self.mat[row_1][ (col_1+1)%5 ]
                cipher_text += self.mat[row_2][ (col_2+1)%5 ]

            else:
                cipher_text += self.mat[row_1][col_2]
                cipher_text += self.mat[row_2][col_1]
            

        return cipher_text.lower()

    def decrypt(self, cipher_text):
        pass