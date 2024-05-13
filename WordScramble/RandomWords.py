
import random
import sys
import nltk

from nltk.corpus import words

#We have switched to using the python nltk (natural language toolkit)
#This will provide us a useful way to produce common words for the
#game to scramble and the user to solve. 

#We have a basic function up and running using the nltk. This is a baseline
#function that the rest of the official game logic will be based on.
#Much more functionality is to come.



def scrambler():
    word_list = words.words()
    while True:
        indy = input("Please enter anything: ")
        if indy:
            random_word = random.choice(word_list)
            if len(random_word) > 5:
                print("yes")
                continue
            elif len(random_word) < 5:
                print("no")
                continue

                
scrambler()
            


    
