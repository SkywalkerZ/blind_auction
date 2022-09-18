import os
from art import logo
print(logo)

end_of_auction= False
auction_dict={}
def add_new_bid(person,amount):
  auction_dict[person]=amount

def highest_bidder(bidding_record):
  highest_bid = 0
  winner=""
  for bidder in auction_dict:
    bid_amount=auction_dict[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner= bidder
  print(f"The winner is {winner}, with a bid of ${highest_bid}")    
    
  
while end_of_auction is False:
  name=input("What is your name?: ").lower()
  bid=int(input("What's your bid?: $"))
  add_new_bid(name,bid)
  choice=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  os.system('clear')

  if choice=='no':
    highest_bidder(auction_dict)
    end_of_auction=True
    print("\nEnd of Auction")
