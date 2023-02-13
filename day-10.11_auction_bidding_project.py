# auction bidding project based on upto days coding knowledge:
# Ranjeet selling his computer and auction is held for this
# create a program for this
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record{"rohan":"₹5k","sohan":"₹10k"}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and its bidding amount is ₹{highest_bid}")


while not bidding_finished:
    name = input("enter your name: ")
    price = int(input("enter your bidding price: ₹"))
    bids[name] = price
    should_continue =  input("are there any other bidder? Type in small leter 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue =="yes":
        bidding_finished = False
        
