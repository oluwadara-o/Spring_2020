import copy
import random

debuging = False
words_list=["happy", "best", "cute", "lovely", "post"]
tries = 10

def pick_word(this_words_list = words_list):
    word = this_words_list[random.randint(0, len(this_words_list)-1)]
    return word

def set_up():
    #remove "word"
    word = pick_word()
    if isinstance(word, str):
        characterlist = list(word)
        if debuging: print(characterlist)
    else:
        raise Exception("Not a word")
    return characterlist


def guess_letter():
    guessed = raw_input("Guess a letter in the word")
    #add exception for valid charcheters
    if guessed in word_list:
        for x in range(len(word_list)):
            letter = word_list[x]
            if guessed == letter:
                blank_list[x] = guessed
                print blank_list
    else:
        print("You Guessed Wrong")
        global tries
        tries -= 1

word_list = set_up()
#blank_list = word_list.copy()
blank_list = copy.copy(word_list)
blank_list = ["_" for x in blank_list]

print (blank_list)


while "_" in blank_list and tries>=0:
    guess_letter()
else:
    if "_" in blank_list:
        print "Dead Man"
        print word_list
    else:
        print "Congratulations! He gets to live another day"