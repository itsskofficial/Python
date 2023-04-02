from pandas import *

data = read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}
nos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

user_input = input("Enter any word of your choice: ")
for alphabet in user_input:
    try:
        for i in nos:
            if i == alphabet:
                raise ValueError("Sorry, only text in input please")
    except ValueError as e:
        print(e)
        break
    else:
        for (key, value) in dict.items():
            if alphabet.upper() == key:
                print(value)
