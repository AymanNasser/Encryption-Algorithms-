from des import DES
import os

def main():
    os.system('clear')
    print("############## DES ##############")

    key = input("Please specifiy the key: ")
    text = input("Please specifiy the text: ")
    n = int(input("No. of times to run the encryption: "))

    des = DES(key)
    
    for i in range(n):
        text = des.encrpyt(text)

    print("Cipher Text: ", text)


if __name__ == "__main__":
    main()

