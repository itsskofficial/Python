import pandas

print("Hello, welcome to Morse Code Converter\n")
user_input=input("Enter your string: ")

code_list=[]
df=pandas.read_csv("code.csv")
df_dict=df.to_dict(orient="records")
for character in user_input:
    for dict in df_dict:
        if dict["Alphabet"]==character.upper():
            code_list.append(dict["Code"])

code=' '.join([element for element in code_list])

print(f"Your morse code is: {code}")
