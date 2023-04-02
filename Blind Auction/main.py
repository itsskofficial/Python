from os import *
from art import *

bids={}
players="Yes"
max_bid=0
winner=""

while players=="Yes":
    system('cls')
    print(logo)
    name=input("\nPlease enter your name: ")
    bid_price=int(input("Please enter your bid price: "))
    bids[name]=bid_price
    players=input("\nAre there more bidders? ")

for name,bid_price in bids.items():
    if bid_price>max_bid:
        max_bid=bid_price
        winner=name
    
print(f"\nThe winner is {winner} whose bid is {max_bid}")




