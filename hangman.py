"""This is a hangman game"""

import random
from wordList import words
import sys
import os
import subprocess

def printHeader():
    print(
            r"""
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
                                                                     

    """
        )

def clearScreen():
    # Clear screen:
    # Linux/macOS
    if os.name == 'posix':
        _= subprocess.call('clear')
    # Windows
    elif os.name == 'nt':
        _= subprocess.call('cls')

while True:  # Main game loop
    # Clear screen
    clearScreen()
    # ASCII title at beginning of game:
    printHeader()
    while True:
        print('How would you like to play?')
        print('(1) I want you to pick the word for me.')
        print('(2) I want to enter my own word.')
        mode = input()
        if mode == '1':
            word = random.choice(words)
            break
        if mode == '2':
            word = input('Enter your word and press enter: ')
            break
        else:
            print('invalid.')
            continue
    wordChars = [*word]
    wordDisplay = []
    guess = ""
    correctGuesses = []
    incorrectGuesses = []
    lives = 12

    for char in wordChars:
        wordDisplay.append("_ ")

    while "_ " in wordDisplay and lives > 0:
        clearScreen()
        printHeader()
        print("\n" * 2)
        print(" ".join(wordDisplay))
        print("correct guesses: " + ", ".join(correctGuesses))
        print("incorrect guesses: " + ", ".join(incorrectGuesses))
        guess = input("Guess a letter (lives remaining: " + str(lives) + "): ")
        if guess not in correctGuesses or guess not in incorrectGuesses:
            for i in range(0, len(wordChars)):
                if wordChars[i] == guess:
                    if guess not in correctGuesses:
                        correctGuesses.append(guess)
                    wordDisplay[i] = guess
            if guess not in incorrectGuesses and guess not in correctGuesses and guess != "":
                incorrectGuesses.append(guess)
                lives = lives - 1
        else:
            print("You already guessed this letter.")
    if lives > 0:
        print("\n" * 2)
        print(" ".join(wordDisplay))
        print("You won with " + lives + " remaining!")
    else:
        print("You lose!")
        print("The word was: " + word)
    print("Play another game? Press 'n' to quit. Any other key to continue.")
    new_game = input()
    if new_game == "n":
        sys.exit()
