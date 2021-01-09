from caesar import Caesar


# Casear test cases
caesar = Caesar(key=3)
print("########## Encryption ##########")
enc_text = caesar.encrpyt("meet me after the toga party")
print(enc_text)
print( enc_text == 'PHHW PH DIWHU WKH WRJD SDUWB'.lower())        

caesar = Caesar(key=23)
enc_text = caesar.encrpyt("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
print(enc_text)
print(enc_text == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")

print("########## Decryption ##########")
cip_text = caesar.decrypt('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')
print(cip_text)
print(cip_text == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')

