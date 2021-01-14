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

    def __shift_cycle_left(self, text, num_bits):
        """
            Shifting left with a cycle approach for any text 
        """
        return text[num_bits:] + text[:num_bits]


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
        shift_bits = des_utils.shift_rounds[round_num-1]
        print("Shift bits", shift_bits)

        left_sub_key = key[:28] 
        right_sub_key = key[28:]

        print("C" + str(round_num-1),left_sub_key)
        print("D" + str(round_num-1), right_sub_key)

        # Shift cycle left
        left_sub_key = self.__shift_cycle_left(left_sub_key, shift_bits)
        right_sub_key = self.__shift_cycle_left(right_sub_key, shift_bits)


        print("C" + str(round_num),left_sub_key == '1110000110011001010101011111')
        print("D" + str(round_num), right_sub_key == '1010101011001100111100011110')
        
        # Permutation choice 2
        key = left_sub_key + right_sub_key
        sub_key = [''] * 48

        for i in range(len(des_utils.pc2)):
            sub_key[i] = key[des_utils.pc2[i]]
        
        print("Circle K of Round: ", round_num)
        return ''.join(sub_key)

    
    def __generate_des_round(self, text, sub_key):
        pass 

    def encrpyt(self, plain_text):
        cipher_text = ""

        # Key
        print("INITIAL KEY: ", self.key)
        key = self.__init_perm_key(self.key)
        print("PC1 Key: ", key) 

        # print(key == '1111000 0110011 0010101 0101111 0101010 1011001 1001111 0001111'.replace(' ', ''))
        sub_key = self.__generate_round_key(key,1)
        


        # plain_text =  self.__init_perm_plain_text(plain_text)
        
        return cipher_text


    def decrypt(self):
        pass