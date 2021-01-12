from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("welcome to the secret auction program")

bidDic = {}
bidding_done = False

def find_winner(bid):
  highest_bid = 0
  winner = ""
  for bidder in bid:
    bid_amount = bid[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_done:
  name = input("what is your name?")
  bid = int(input("What is your bid?"))
  bidDic[name] = bid

  yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if yes_or_no == "no":
    bidding_done = True
    find_winner(bidDic)
  elif yes_or_no:
    clear()
  