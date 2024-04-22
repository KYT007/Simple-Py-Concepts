from random_word import RandomWords
import random
import sys

#This game will step up difficulty in levels. This is level one.
def scramble_word_level_1(word):
    while True:
        word = list(word)
        random.shuffle(word)
        scrambled_word = ''.join(word)
        return scrambled_word

def word_scramble_level_2(word):
    pass
    # This game will step up difficulty in levels. This will be for level 2.

def play_game():
    r = RandomWords()
    while True:
        print("okay, lets play...can you unscramble the word?")
        taskword = r.get_random_word()
        if taskword and len(taskword) > 5:
            break
        scrambled_taskword = scramble_word_level_1(taskword)
        print(scrambled_taskword)
        print(taskword)
        
        
        solve_guess = input("Can you unscramble the above word? Enter here: ")

        if solve_guess == taskword:
            print("nice, you got it!")
            continue
        else:
            print("Nope, wrong!")
            sys.exit()


play_game()