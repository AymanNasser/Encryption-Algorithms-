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
    
    def __from_int_to_binary(self, num):
        return str(bin(num)[2:])


    def __from_binary_to_hex(self, num):
        return str(hex(int(num, 2))[2:]).zfill(16)



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
        
        # print("C" + str(round_num-1),left_sub_key)
        # print("D" + str(round_num-1), right_sub_key)



        # print("C" + str(round_num),left_sub_key == '1110000110011001010101011111')
        # print("D" + str(round_num), right_sub_key == '1010101011001100111100011110')
        
        # Permutation choice 2
        sub_key = [''] * 48

        for i in range(len(des_utils.pc2)):
            sub_key[i] = key[des_utils.pc2[i]]
        
        # print("Round Key" + str(round_num), ": ", sub_key)
        return ''.join(sub_key)


    def __expand_text(self, text):
        expanded_right_text = [''] * 48
        for i in range(48):
            expanded_right_text[i] = text[des_utils.expansion_table[i]]

        return ''.join(expanded_right_text)

    
    def __xor(self, text_1, text_2 ):
        assert len(text_1) == len(text_2) , 'Text lengths does not match'

        xored_text = [''] * len(text_1)
        for i in range(len(text_1)):
            xored_text[i] = str(int(text_1[i], 2) ^ int(text_2[i], 2))

        return ''.join(xored_text)

    def __substitue_s_box(self, text):
        s_boxed_text = []
        for i in range(0,48,6):
            s_boxed_text.append(text[i:i+6]) 

        for i in range(8):
            row = int(s_boxed_text[i][0] + s_boxed_text[i][-1], 2)
            col = int(s_boxed_text[i][1:5], 2)

            s_boxed_text[i] = self.__from_int_to_binary(des_utils.sbox[i][row][col])
            s_boxed_text[i] = str(s_boxed_text[i]).zfill(4)

            # print("OUT SBOX: " + s_boxed_text[i])   

        # print ("FINAL S_BOXED", ''.join(s_boxed_text))
        return ''.join(s_boxed_text)        
    

    def __transposition_p_box(self, text):
        transpoed_text = [''] * 32
        for i in range(32):
            transpoed_text[i] = text[des_utils.p[i]]

        return ''.join(transpoed_text)


    def __generate_des_round(self, text, sub_key, round_num):
        left_sub_text = text[:32]
        right_sub_text = text[32:]

        # Expansion
        expanded_right_text = self.__expand_text(right_sub_text)
        # print(len(expanded_right_text))

        # Xoring key with expanded text 
        xored_text = self.__xor(expanded_right_text, sub_key)
        # print(len(xored_text))

        # S-box
        substituted_text = self.__substitue_s_box(xored_text)
        # print(len(substituted_text))

        # P-box
        p_box_text = self.__transposition_p_box(substituted_text)

        # Xoring key with left text
        final_right_sub_text = self.__xor(left_sub_text, p_box_text)
        
        output_text = right_sub_text + final_right_sub_text

        return output_text


    def __final_permutation(self, text):
        final_text = [''] * 64
        for i in range(64):
            final_text[i] = text[des_utils.fp[i]]
        
        return ''.join(final_text)

    def encrpyt(self, plain_text):

        # Key
        # print("INITIAL KEY: ", self.key)
        key = self.__init_perm_key(self.key)
        # print("PC1 Key: ", key) 

        # print(key == '1111000 0110011 0010101 0101111 0101010 1011001 1001111 0001111'.replace(' ', ''))
        
        # print(sub_key == ' 000110 110000 001011 101111 111111 000111 000001 110010'.replace(' ', ''))

        text =  self.__init_perm_plain_text(plain_text)
        # print(plain_text == '1100 1100 0000 0000 1100 1100 1111 1111 1111 0000 1010 1010 1111 0000 1010 1010'.replace(' ', ''))
        
        for round in range(16):
            
            # Key processing
            shift_bits = des_utils.shift_rounds[round]
            left_sub_key = key[:28] 
            right_sub_key = key[28:]

            # Shift cycle left
            left_sub_key = self.__shift_cycle_left(left_sub_key, shift_bits)
            right_sub_key = self.__shift_cycle_left(right_sub_key, shift_bits)

            key = left_sub_key + right_sub_key

            sub_key = self.__generate_round_key(key, round)

            # Text processing
            text = self.__generate_des_round(text, sub_key, round)
        
        
        # Bit-Swap
        print(text == '0100001101000010001100100011010000001010010011001101100110010101')

        text = text[32:] + text[:32]
        print(text == '0000101001001100110110011001010101000011010000100011001000110100')

        # Final permutation
        cipher_text = self.__final_permutation(text)

        return self.__from_binary_to_hex(cipher_text).upper()


    def decrypt(self):
        pass