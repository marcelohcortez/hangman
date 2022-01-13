import random
from words import wordsList
import string

def get_valid_words(wordsList):
    word = random.choice(wordsList)
    return word.upper()

def hangman():
    chosenWord = get_valid_words(wordsList)
    wordLetters = set(chosenWord)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 7

    while len(wordLetters) > 0 and lives > 0:
        wordList = [letter if letter in usedLetters else '-' for letter in chosenWord]
        
        print(f'You have {lives} lives left.\nYou already used these letters: {" ".join(usedLetters)}\n')
        print(f'Current word: {" ".join(wordList)}\n')

        userLetter = input('Guess a letter: ').upper()
        
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print('')
            else:
                lives = lives - 1
                print(f'\nThe letter {userLetter.upper()} is not in the word.\n')
        
        elif userLetter in userLetter:
            print(f'\nThe letter {userLetter.upper()} was already used.\n')
        
        else:
            print(f'\nThe character {userLetter.upper()} is not valid.\n')
    
    if lives == 0:
        print(lives)
        print(f'\nYou lost.\nThe word was {chosenWord}.\nTry again.\n')
    else:
        print(f'You made it!\n The word was {chosenWord}.\n')

hangman()