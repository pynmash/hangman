"""This is a hangman game"""

import random
from wordList import words


while True:  # Main game loop
    # ASCII title at beginning of game:
    print(
        r""" ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
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
    word = random.choice(words)
    wordChars = [*word]
    wordDisplay = []
    guess = ""
    correctGuesses = []
    incorrectGuesses = []
    lives = 12

    for char in wordChars:
        wordDisplay.append("_ ")

    while "_ " in wordDisplay and lives > 0:
        print("\n" * 2)
        print(" ".join(wordDisplay))
        print("correct guesses: " + str(correctGuesses))
        print("incorrect guesses: " + str(incorrectGuesses))
        guess = input("Guess a letter (lives remaining: " + str(lives) + "): ")
        if guess not in correctGuesses or guess not in incorrectGuesses:
            for i in range(0, len(wordChars)):
                if wordChars[i] == guess:
                    if guess not in correctGuesses:
                        correctGuesses.append(guess)
                    wordDisplay[i] = guess
            if (
                guess not in incorrectGuesses
                and guess not in correctGuesses
                and guess != ""
            ):
                incorrectGuesses.append(guess)
                lives = lives - 1
        else:
            print("You already guessed this letter.")
    if lives > 0:
        print("\n" * 2)
        print(" ".join(wordDisplay))
        print("You won!")
    else:
        print("You lose!")
        print("The word was: " + word)
