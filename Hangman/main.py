from typing import DefaultDict
from hangman_art import *
from hangman_words import *
import random, os

print(logo)
print ("\nWelcome to Hangman!\n")
choosen_word=random.choice(word_list)
display=[]
lives=6
start=stages[-1]
j=len(choosen_word)
for i in range(1,len(choosen_word)+1):
    display.append('_')
print(display)
k=len(choosen_word)
print (start)
while k!=0 and lives!=0:
    guess=input("\nPLease guess a letter: ").lower()
    os.system('cls')
    if guess in display:
        print(f"You have already guessed the letter {guess}")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
            k-=1
        elif letter != guess:
            j-=1
    if j==0:
        print(f"Your guessed letter {guess} is not in the word, you lost a life\n")
        lives-=1   
        print(f"Lives remaining: {lives}")
    print(stages[lives])
    print (display)
    j=len(choosen_word)
if k==0:
    print("\nYou win!")
    print("You guessed the word %s" %choosen_word)
elif lives==0:
    print("\nYou lose")
    print("The word was %s" %choosen_word)



