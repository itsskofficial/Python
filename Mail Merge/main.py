# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_stri

f1 = open("./Input/Letters/starting_letter.txt")
starting_letter = f1.read()
f2 = open("./Input/Names/invited_names.txt")
names = f2.readlines()
i = 0
for name in names:
    names[i] = name.strip("\n")
    i += 1
for name in names:
    letter = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as f3:
        f3.write(letter)
