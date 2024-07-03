import random

'''This is a simple blackjack game! It doesn't quite adhere to all the rules of 
real life blackjack. Its meant as an exercise to get the hang of flow control
and functions that return things.'''

'''A function that deals initial cards to the user and the bot/computer'''
def deal_card():
    draw_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    new_card = random.choice(draw_deck)
    return new_card
    
'''Calculation score that assists with converting aces to a 1 in hands that have an ace and are over 21!'''
def calculate_score(player_cards):
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
    return sum(player_cards)

'''Function to compare scores and determine a winner'''
def compare(usersscore, computersscore):
    if usersscore > 21 and computersscore > 21:
        return "You went over. You lose "


    if usersscore == computersscore:
        return "Draw "
    elif computersscore == 0:
        return "Lose, opponent has Blackjack "
    elif usersscore == 0:
        return "Win with a Blackjack "
    elif usersscore > 21:
        return "You went over. You lose "
    elif computersscore > 21:
        return "Opponent went over. You win "
    elif usersscore > computersscore:
        return "You win "
    else:
        return "You lose "
    

    

def Play():
    
    
    is_game_over = False

    user_cards = []
    bot_cards = []


    for _ in range(2):
        user_cards.append(deal_card())
        bot_cards.append(deal_card())

    while not is_game_over:   
                
        bot_score = calculate_score(bot_cards)
        user_score = calculate_score(user_cards)
        print(f'Current hands: {bot_cards, user_cards}')        


        if user_score == 0 or bot_score == 0 or user_score > 21:
            is_game_over = True
        else: draw_again = input('You wanna draw a card or stand? y for draw, /n for stand: ')
        if draw_again == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            is_game_over = True

    while bot_score != 0 and bot_score < 17:
        bot_cards.append(deal_card())
        bot_score = calculate_score(bot_cards)

        print(compare(user_score, bot_score))
    
    while input("Do you want to play blackjack? y or n: ") == 'y':
        Play()
Play()