import time, random, sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors!")
time.sleep(3)
print ("Lets Start!")
time.sleep(1)
user=int(input("What do you choose?\nType 1 for Rock, 2 for Paper, 3 for Scissors: "))
if user==1:
    print(f"You chose:\n{rock}")
elif user==2:
    print(f"You chose:\n{paper}")
elif user==3:
    print(f"You chose:\n{scissors}")
else:
    print("Please choose a valid option, try again!")
    sys.exit()

computer=random.randint(1,3)
if computer==1:
    print(f"Computer chose:\n{rock}")
elif computer==2:
    print(f"Computer chose:\n{paper}")
else:
    print(f"Computer chose:\n{scissors}")

if user==computer:
    print("Its a tie!")
elif user==1 and computer==2:
    print ("You lose!")
elif user==1 and computer==3:
    print ("You win!")
elif user==2 and computer==1:
    print ("You win!")
elif user==2 and computer==3:
    print ("You lose!")
elif user==3 and computer==2:
    print ("You win!")
elif user==3 and computer==1:
    print ("You lose!")


