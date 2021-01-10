from caesar import Caesar
from play_fair import Playfair

# Casear test cases
# caesar = Caesar(key=3)
# print("########## Encryption ##########")
# enc_text = caesar.encrpyt("meet me after the toga party")
# print(enc_text)
# print( enc_text == 'PHHWPHDIWHUWKHWRJDSDUWB'.lower())        

# caesar = Caesar(key=23)
# enc_text = caesar.encrpyt("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
# print(enc_text)
# print(enc_text == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")

# caesar = Caesar(key=6)
# print("########## Decryption ##########")
# cip_text = caesar.decrypt('PHHW PH DIWHU WKH WRJD SDUWB')
# print(cip_text)
# print(cip_text == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')


# PlayFair test cases
pl_f = Playfair(keyword='LARGEST')
# print(pl_f._letter_location)
# print(pl_f.encrpyt("Must see you over Cadogan. West Coming at once."))
# print("UZ TB DL GZ PN NW LG TG TU ER OV LD BD UH FP ER HW QS RZ")
print(pl_f.encrpyt('mu st# ee yor'))

