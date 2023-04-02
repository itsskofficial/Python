#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))
level=int(input("Type 1 for a easy password and 2 for a hard one: "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass1=[]
for i in range(1,nr_letters+1):
    j=random.choice(letters)
    pass1.append(j)
pass2=[]
for i in range(1,nr_symbols+1):
    j=random.choice(symbols)
    pass2.append(j)
pass3=[]
for i in range(1,nr_numbers+1):
    j=random.choice(numbers)
    pass3.append(j)
password=""
pass4=pass1 + pass2 + pass3
length=len(pass4)
if level==1:
    for i in pass1:
        password += i
    for i in pass2:
        password += i
    for i in pass3:
        password += i
elif level==2:
    for i in range(0,length):
        j=random.choice(pass4)
        password+=j
        pass4.remove(j)
else:
    print ("Please select valid option, try again!")
print (f"\nYour password is {password}")
