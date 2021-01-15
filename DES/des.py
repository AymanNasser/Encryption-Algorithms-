from cipher import Cipher
import des_utils
import re

class DES(Cipher):
    def __init__(self, key):
        self.key = key

    def __from_hex_to_binary(self, num):
        """
        Converts a hex decimal number to binary representation

        Args: Hex decimal number

        Return: Binary representation of that number
        """

        # {} places a variable into a string
        # 0 takes the variable at argument position 0
        # : adds formatting options for this variable (otherwise it would represent decimal 6)
        # 064 formats the number to 64 digit zero-padded on the left
        # b converts the number to its binary representation

        return '{0:064b}'.format(int(num, 16))
    
    def __from_int_to_binary(self, num):
        """
        Converting an int number to binary representation 
        """
        return str(bin(num)[2:])


    def __from_binary_to_hex(self, num):
        """
        Converting a binary representation number to hex   
        """
        return str(hex(int(num, 2))[2:]).zfill(16)


    def __shift_cycle_left(self, text, num_bits):
        """
        Shifting left with a cycle approach for any text 
        """
        return text[num_bits:] + text[:num_bits]


    def __init_perm_plain_text(self, plain_text):
        """
        Performing initial permutation to the plain text
        """
        plain_text = self.__from_hex_to_binary(plain_text)
        permuted_text = [''] * 64

        for i in range(len(des_utils.ip)):
            permuted_text[i] = plain_text[des_utils.ip[i]]
        
        return ''.join(permuted_text)


    def __init_perm_key(self,key):
        """
        Performing initial permutation to the key
        """
        key = self.__from_hex_to_binary(key)
        permuted_key = [''] * 56

        for i in range(len(des_utils.pc1)):
            permuted_key[i] = key[des_utils.pc1[i]]

        return ''.join(permuted_key)


    def __generate_round_key(self, key, round_num):
        """
        Generating a key for each round

        Args: 
            key: 56 bit left circular shifted sub_key 
            round_num: An int which ranges from 0 to 15 

        Return:
            sub_key: 48 bit sub_key
        """
        # Permutation choice 2
        sub_key = [''] * 48

        for i in range(len(des_utils.pc2)):
            sub_key[i] = key[des_utils.pc2[i]]
        
        return ''.join(sub_key)


    def __expand_text(self, text):
        """
        Expanding right sub text from 32 bit to 48 bit
        """
        expanded_right_text = [''] * 48
        for i in range(48):
            expanded_right_text[i] = text[des_utils.expansion_table[i]]

        return ''.join(expanded_right_text)

    
    def __xor(self, text_1, text_2 ):
        """
        Xoring 2 binary numbers
        """
        assert len(text_1) == len(text_2) , 'Text lengths does not match'

        xored_text = [''] * len(text_1)
        for i in range(len(text_1)):
            xored_text[i] = str(int(text_1[i], 2) ^ int(text_2[i], 2))

        return ''.join(xored_text)


    def __substitue_s_box(self, text):
        """
        Applying s-box transpostions
        """
        s_boxed_text = []
        for i in range(0,48,6):
            s_boxed_text.append(text[i:i+6]) 

        for i in range(8):
            row = int(s_boxed_text[i][0] + s_boxed_text[i][-1], 2)
            col = int(s_boxed_text[i][1:5], 2)

            s_boxed_text[i] = self.__from_int_to_binary(des_utils.sbox[i][row][col])
            s_boxed_text[i] = str(s_boxed_text[i]).zfill(4)

        return ''.join(s_boxed_text)        
    

    def __transposition_p_box(self, text):
        """
        Applying p-box permutations
        """
        transpoed_text = [''] * 32
        for i in range(32):
            transpoed_text[i] = text[des_utils.p[i]]

        return ''.join(transpoed_text)


    def __generate_des_round(self, text, sub_key, round_num):
        """
        Generating a DES round 
        """
        left_sub_text = text[:32]
        right_sub_text = text[32:]

        # Expansion
        expanded_right_text = self.__expand_text(right_sub_text)

        # Xoring key with expanded text 
        xored_text = self.__xor(expanded_right_text, sub_key)

        # S-box
        substituted_text = self.__substitue_s_box(xored_text)

        # P-box
        p_box_text = self.__transposition_p_box(substituted_text)

        # Xoring key with left text
        final_right_sub_text = self.__xor(left_sub_text, p_box_text)
        
        output_text = right_sub_text + final_right_sub_text

        return output_text


    def __final_permutation(self, text):
        """
        Applying ip-1
        """
        final_text = [''] * 64
        for i in range(64):
            final_text[i] = text[des_utils.fp[i]]
        
        return ''.join(final_text)

    def encrpyt(self, plain_text):
        # Removing all the characters except numbers and alphabets 
        self.key = re.sub('[\W_]+', '',self.key)
        plain_text = re.sub('[\W_]+', '', plain_text)
        
        # Initial Permutation
        key = self.__init_perm_key(self.key)
        text =  self.__init_perm_plain_text(plain_text)
    
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
        text = text[32:] + text[:32]

        # Final permutation
        cipher_text = self.__final_permutation(text)

        return self.__from_binary_to_hex(cipher_text).upper()


    def decrypt(self):
        pass