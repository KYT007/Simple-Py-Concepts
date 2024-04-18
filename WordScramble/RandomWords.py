from random_word import RandomWords
import random

def scramble_word_level_1(word):
    word = list(word)
    random.shuffle(word)
    scrambled_word = ''.join(word)
    return scrambled_word

def word_scramble_level_2(word):
    pass