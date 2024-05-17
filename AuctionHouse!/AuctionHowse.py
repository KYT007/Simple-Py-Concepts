import pyinputplus as pyip

#Today we build an auction house game to practice working with dicitonaries and lists,
#specifically lists of dictionary vallues.

def start_auction():
    bidding_finished = False
    bids = {}

    while not bidding_finished:
        print('Welcome to the auction house! Today we are bidding on a flood damaged 2014 Camaro. It still runs!')
        name = pyip.inputStr('What is your name?: ')

        bid = pyip.inputInt('What is your bid?: ')

        bids[name] = bid

        yOn = pyip.inputStr('Are there any bidders left?')

        if yOn.lower() == 'yes':
            continue
        if yOn.lower() == 'no':
            bidding_finished = True
            for i in bids.items():
                print(i)
            
        


start_auction()