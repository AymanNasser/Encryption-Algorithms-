from caesar import Caesar
from play_fair import Playfair
from hill import Hill
from vigenere import Vigenere
from vernam import Vernam
import utils
import re

INPUT_PATH = '../inputs'
OUTPUT_PATH = '../results'

def fill_files():

    # Caesar
    keys = [3,6,12]
    with open(INPUT_PATH + '/Caesar/caesar_plain.txt', 'r') as file:
        lines = file.readlines()

    with open(OUTPUT_PATH + '/caesar.txt', 'w+') as file:
        for key in keys:
            caesar = Caesar(key)
            file.write('Key: ' + str(key) + '\n')

            for plain_text in lines:
                file.write(caesar.encrpyt(plain_text) + '\n')
                

    # Playfair
    keys = ['rats', 'archangel'] 
    with open(INPUT_PATH + '/PlayFair/playfair_plain.txt', 'r') as file:
        lines = file.readlines()
    
    with open(OUTPUT_PATH + '/playfair.txt', 'w+') as file:
        for key in keys:
            play_fair = Playfair(key)
            file.write('Key: ' + str(key) + '\n')

            for plain_text in lines:
                file.write(play_fair.encrpyt(plain_text) + '\n')

    # Hill
    key = [[5,17], [8,3]] 
    with open(INPUT_PATH + '/Hill/hill_plain_2x2.txt', 'r') as file:
        lines = file.readlines()

    with open(OUTPUT_PATH + '/hill_2x2.txt', 'w+') as file:
        hill = Hill(key)
        file.write('Key: ' + str(key) + '\n')
        for plain_text in lines:
            file.write(hill.encrpyt(plain_text) + '\n')

    key = [[2,4,12], [9,1,6], [7,5,3]]
    with open(INPUT_PATH + '/Hill/hill_plain_3x3.txt', 'r') as file:
        lines = file.readlines()

    with open(OUTPUT_PATH + '/hill_3x3.txt', 'w+') as file:    
        hill = Hill(key)
        file.write('Key: ' + str(key) + '\n')
        for plain_text in lines:
            file.write(hill.encrpyt(plain_text) + '\n')
    # Vigenere
    key = ['pie', 'aether']
    mode = [True, False]
    with open(INPUT_PATH + '/Vigenere/vigenere_plain.txt', 'r') as file:
        lines = file.readlines()
    
    with open(OUTPUT_PATH + '/vigenere.txt', 'w+') as file:
        for i in range(2):
            file.write('Key: ' + str(key[i]) + '\nMode: ' + str(mode[i]) + '\n')
            vig = Vigenere(key[0], mode[0])
            for plain_text in lines:
                file.write(vig.encrpyt(plain_text) + '\n')
    # Vernam
    key = 'SPARTANS'
    with open(INPUT_PATH + '/Vernam/vernam_plain.txt', 'r') as file:
        lines = file.readlines()
    
    with open(OUTPUT_PATH + '/vernam.txt', 'w+') as file:
        file.write('Key: ' + str(key) + '\n')
        ver = Vernam(key)
        for plain_text in lines:
            file.write(ver.encrpyt(plain_text))


def main():
    print("############## Classical Ciphers ##############")
    fill_files()


if __name__ == "__main__":
    main()