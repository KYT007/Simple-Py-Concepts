from random import randint
import pyinputplus as pyip
import sys

def get_input(prompt):
    while True:
        user_input = input(prompt)
        
        if user_input.upper() == 'Q':
            print("Exiting...")
            return user_input
        
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'Q' to quit.")


def play_game():
    print("Welcome to the random numbers game! Lets get this going!")
    while True:
        low_bounds = get_input("Please enter lower bounds: ")
        up_bounds = get_input("Please enter upper bounds: ")
        if low_bounds >= up_bounds:
            print(f"Invalid! High bounds must be greater than low/low bounds must be less than high!")
            continue
        magic_num = randint(low_bounds, up_bounds)
        tries = 1
        while tries < 7:
            guess = get_input(f"Please guess a number between {low_bounds} and {up_bounds}: ")
            if guess < magic_num:
                print(f"Too low!")
                tries += 1
            elif guess > magic_num:
                print(f"Too high!")
                tries += 1
            else:
                if guess == magic_num:
                    print(f"You got it! You guessed it in {tries} tries!")
                    break
        if tries == 7:
            tries = 1
            print(f"Sorry, you didn't guess the number in enough tries. Game over! Try again?")
        answer = pyip.inputChoice(['Yes', 'No'])
        if answer == 'Yes':
            break
        else:
            if answer == 'No':
                print(f"Ok, thanks for playing! Seeya!")
                sys.exit()
                
play_game()