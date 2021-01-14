from cipher import Cipher
import des_utils
import re
from collections import deque

class DES(Cipher):
    def __init__(self, key):
        self.key = key

    def __from_hex_to_binary(self, num):
        """
            Converts a hex decimal number to binary representation

            Args: Hex decimal number

            Return: Binary represtation of that number

        """

        # {} places a variable into a string
        # 0 takes the variable at argument position 0
        # : adds formatting options for this variable (otherwise it would represent decimal 6)
        # 064 formats the number to 64 digit zero-padded on the left
        # b converts the number to its binary representation

        return '{0:064b}'.format(int(num, 16))


    def __init_perm_plain_text(self, plain_text):
        plain_text = self.__from_hex_to_binary(plain_text)
        permuted_text = [''] * 64

        for i in range(len(des_utils.ip)):
            permuted_text[i] = plain_text[des_utils.ip[i]]
        
        return ''.join(permuted_text)


    def __init_perm_key(self,key):
        key = self.__from_hex_to_binary(key)
        permuted_key = [''] * 56

        for i in range(len(des_utils.pc1)):
            permuted_key[i] = key[des_utils.pc1[i]]

        return ''.join(permuted_key)


    def __generate_round_key(self, key, round_num):
        shift_bits = des_utils.fp[round_num-1]
        
        left_sub_key = deque(list(key[:28])) 
        right_sub_key = deque(list(key[28:]))

        print(left_sub_key)
        print(right_sub_key)

        left_sub_key = str(left_sub_key.rotate(-shift_bits))
        right_sub_key = str(right_sub_key.rotate(-shift_bits))
        sub_key = left_sub_key + right_sub_key
        
        print("Circle K")
        return sub_key

    
    def __generate_des_round(self, text, sub_key):
        pass 

    def encrpyt(self, plain_text):
        cipher_text = ""

        # plain_text =  self.__init_perm_plain_text(plain_text)
        key = self.__init_perm_key(self.key)

        # print(key) 
        # print(key == '1111000 0110011 0010101 0101111 0101010 1011001 1001111 0001111'.replace(' ', ''))
        print(self.__generate_round_key(key,1))
        return cipher_text


    def decrypt(self):
        pass