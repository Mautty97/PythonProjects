'''
This program will take a string input by the user and then convert it into Pig Latin:
by moving the first letter to the end and adding the suffix -ay (ex: banana => ananabay)
Author: Mautty97 (https://github.com/Mautty97)
Inspiration: https://github.com/karan/Projects
'''
import string

def get_input():
    #get user input
    sentence = input("What would you like to say in Pig Latin: ")
    #return user input
    return sentence

def pl_converter(user_sentence):

    #remove punctuation
    cleaned_sentence = user_sentence.translate(str.maketrans('', '', string.punctuation))

    #split sentance into words
    words = cleaned_sentence.split()
    
    #convert word
    pl_list = []
    j = 0
    for word in words:
        word = word.lower()
        i = len(word)
        pl_word = f"{word[1:i]}{word[0]}ay"
        #capitalize the first word in the new sentance
        if j==0:
            pl_word = pl_word.capitalize()
        #append word to list
        pl_list.append(f"{pl_word} ")
        j += 1

    #create new string from list
    pl_sentence = ""
    for word in pl_list:
        pl_sentence += word
        
    #return new string
    return pl_sentence

'''Main Code'''
print(pl_converter(get_input()))