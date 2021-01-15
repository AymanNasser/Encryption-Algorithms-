from des import DES

des = DES('133457799BBCDFF1')
encrypted_text = des.encrpyt('0123456789ABCDEF')
print(encrypted_text)
print(encrypted_text == '85E813540F0AB405')
# st_ = 'abdefgh'
# print(st_[2:] + st_[:2])

# z = '123456789ABCDEF'
# print('{0:064b}'.format(int(z,16)), type('{0:064b}'.format(int(z,16))))

# print(int('0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'.replace(' ', ''), 2))

# print(hex(int('00011110', 2)))