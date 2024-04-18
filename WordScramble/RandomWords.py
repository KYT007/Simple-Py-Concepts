from random_word import RandomWords
import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    scrambled_word = ''.join(word)
    return scrambled_word