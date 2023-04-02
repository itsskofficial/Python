from art import *
from caesar import *

i=1

while i==1:
    print ("\n %s" %logo)
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))   
    caesar(direction,text,shift)
    choice=input("\nDo ypou want to play again? ")
    if choice=="no":
        i=0
        


    