from des import DES

# des = DES('0000000000000000')
# encrypted_text = des.encrpyt('FFFFFFFFFFFFFFFF')
# print(encrypted_text)
# print(encrypted_text == '355550B2150E2451')
# encrypted_text = des.encrpyt(encrypted_text)
# print(encrypted_text)
# print(encrypted_text == 'FFFFFFFFFFFFFFFF')

# des = DES('01 23 45 67 89 AB CD EF'.replace(' ', ''))
# encr_text = des.encrpyt('01 23 45 67 89 AB CD EF'.replace(' ', ''))
# print(encr_text == '56 CC 09 E7 CF DC 4C EF'.replace(' ', ''))
# print(encr_text)

# des = DES('01 23 45 67 89 AB CD EF'.replace(' ', ''))
# cip_text = des.decrypt('56 CC 09 E7 CF DC 4C EF'.replace(' ', ''))
# print(cip_text, cip_text == '01 23 45 67 89 AB CD EF'.replace(' ', ''))

# des = DES('0000000000000000')
# cip_text = des.decrypt('355550B2150E2451')
# print(cip_text)