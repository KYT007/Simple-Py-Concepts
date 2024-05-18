import pyinputplus as pyip
import sys
import os

'''today we build an auction house game to practice working with dicitonaries and lists,
specifically lists of dictionary vallues.'''

def Clear():
    os.system('clear')

def start_auction():
    bids = {}
    bidding_finished = False
    print('Welcome to the auction house! Today we are bidding on a flood damaged 2014 Camaro. It still runs!')

    #we start our auction with bidding finished set to false


    while not bidding_finished:
        #pyinputplus is very handy for these simple CLI programs

        
        name = pyip.inputStr('Enter Your Name: ')
        

        bid = pyip.inputInt('Enter Your Bid: ')

        bids[name] = bid
        Clear()

        yOn = pyip.inputStr('Are there any bidders left? Yes/No: ')

        if yOn.lower() == 'no':
            bidding_finished = True
            find_winner(bids)
            #if bidding is done
    
        elif yOn.lower() == 'yes':
            continue
            #if bidding is not done
            
        ''''Here we take the bids, the bids are stored in the dictionary "bids"'''
            
        
        
def find_winner(bid_record):
    '''This is our function to calculate the winner. We store a winer variable set to 0,
    loop through the dictionary of bidders and bids, we check which is the highest via >, and
    print it out'''
    winning_bid = 0
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > winning_bid: 
            winning_bid = bid_amount
            winner = bidder
    print(f'Our winner is {winner} with a bid of ${winning_bid}. Thanks for coming out! Now get this heap off our lot!')
    sys.exit()
            
        

        
        

start_auction()