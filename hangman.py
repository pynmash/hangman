"""This is a hangman game"""

import os
import random
import subprocess
import sys

from wordList import words


def print_header():
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
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░"""
    )


def clear_screen():
    # Linux/macOS
    if os.name == "posix":
        subprocess.call("clear")
    # Windows
    elif os.name == "nt":
        os.system("cls")


while True:  # Main game loop
    clear_screen()
    print_header()
    while True:
        print("How would you like to play?")
        print("(1) I want you to pick the word for me.")
        print("(2) I want to enter my own word.")
        mode = input()
        if mode == "1":
            word = random.choice(words)
            break
        if mode == "2":
            while True:
                word = input("Enter your word and press enter: ")
                if word.isalpha():
                    break
                else:
                    print(
                        "Please only use letters. Numbers and special' \
                        'characters are not allowed"
                    )
            break
        else:
            print("invalid.")
            continue
    wordChars = [*word]
    wordDisplay = []
    GUESS = ""
    correctGUESSes = []
    incorrectGUESSes = []
    LIVES = 12
    for char in wordChars:
        wordDisplay.append("_ ")
    while "_ " in wordDisplay and LIVES > 0:
        clear_screen()
        print_header()
        print("\n" * 2)
        print(" ".join(wordDisplay))
        print("correct GUESSes: " + ", ".join(correctGUESSes))
        print("incorrect GUESSes: " + ", ".join(incorrectGUESSes))
        while True:
            GUESS = input("guess a letter (lives remaining: " + str(LIVES) + "): ")
            if len(GUESS) != 1:
                print("1 letter at a time please.")
            else:
                if not GUESS.isalpha():
                    print(
                        "Please only use letters. Numbers and special"
                        "characters are not allowed"
                    )
                break
        GUESS = GUESS.lower()
        if GUESS not in correctGUESSes or GUESS not in incorrectGUESSes:
            for i in range(0, len(wordChars)):
                if wordChars[i] == GUESS:
                    if GUESS not in correctGUESSes:
                        correctGUESSes.append(GUESS)
                    wordDisplay[i] = GUESS
            if (
                GUESS not in incorrectGUESSes
                and GUESS not in correctGUESSes
                and GUESS != ""
            ):
                incorrectGUESSes.append(GUESS)
                LIVES -= 1
        else:
            print("You already GUESSed this letter.")
    if LIVES > 0:
        print("\n" * 2)
        print(
            r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⢲⣏⢨⣽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣾⠃⢙⢴⣞⡟⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣻⠡⣀⣄⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⠉⣷⣿⢠⣍⣉⠉⠐⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠏⠏⠸⡄⢻⡏⣏⠀⠂⠄⠀⣈⠒⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡈⠁⠹⠆⠄⢀⣼⠻⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢈⣳⠆⣀⣄⣼⠴⠚⠁⠀⠀⢀⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣖⠊⠉⠸⣿⣷⡄⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣠⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠲⠬⢿⣿⣦⣤⣄⠀⠈⣿⣿⣟⣛⣩⢿⠀⠀⠀⣠⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣤⣏⢻⣭⣿⡝⢹⣤⣶⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⢻⣿⡄⢿⣿⢁⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡘⠇⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠗⠚⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣛⠿⢿⡫⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣦⣤⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣦⣾⣇⢹⣶⣿⢁⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣿⣿⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡄⣿⡇⣼⣿⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡏⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣜⣸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣟⠉⢙⣿⣿⣿⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠈⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⢻⣭⣭⡿⣻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡞⣿⣿⢳⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠁⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⢻⣿⣿⡸⣏⣾⣿⡟⣿⣷⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠿⢻⣿⣿⣿⡇⣿⣿⣿⡿⠸⠿⠇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡏⠀⠀⢿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⣾⣿⣿⠷⠺⣿⣿⡇⢸⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⣿⣿⣿⡿⠀⠀⠀⠀⠀⡞⠉⠉⠉⠉⣽⣿⣿⡏⠉⠉⢹⣿⣿⣿⠉⠉⠉⠉⢹⡀⠀⠀⢸⣿⡇⣿⣿⣿⣦⣴⣿⣿⡇⢸⣿⡷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠈⠛⠟⠃⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠈⣇⠀⠀⢸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣧⠰⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⣏⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣹⠀⠀⢸⣿⡇⣿⣿⣿⡏⢹⣿⣿⣯⠸⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡇⣿⣿⣿⡿⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡤⠤⠤⠤⠤⣿⣿⣿⡧⣿⣿⣿⡧⠤⠤⠤⠤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⠋⠀⠀⠀⠀⠀⠻⣿⣿⠇⠻⣿⣿⠃⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡟⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠛⠀⠀⠀⠀⠀⠀⠀⠀⡴⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⣀⣽⣿⣿⣧⣸⣿⣿⣧⣀⣀⣀⣀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⢸⣿⣿⡏⢸⣿⣿⡿⠀⠀⠀⠈⠣⡀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠉⠋⠁⠀⠉⠋⠀⠀⠀⠀⠀⠀⠙⢄⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠟⠉⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠿⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠬⢷⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣽⡋⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⡾⠟⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀
    """
        )
        print(" ".join(wordDisplay))
        print("You won with " + str(LIVES) + " lives remaining!")
    else:
        print(
            r'''
                         uuuuuuu
                     uu$$$$$$$$$$$uu
                  uu$$$$$$$$$$$$$$$$$uu
                 u$$$$$$$$$$$$$$$$$$$$$u
                u$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$"   "$$$"   "$$$$$$u
               "$$$$"      u$u       $$$$"
                $$$u       u$u       u$$$
                $$$u      u$$$u      u$$$
                 "$$$$uu$$$   $$$uu$$$$"
                  "$$$$$$$"   "$$$$$$$"
                    u$$$$$$$u$$$$$$$u
                     u$"$"$"$"$"$"$u
          uuu        $$u$ $ $ $ $u$$       uuu
         u$$$$        $$$$$u$u$u$$$       u$$$$
          $$$$$uu      "$$$$$$$$$"     uu$$$$$$
        u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
         """      ""$$$$$$$$$$$uu ""$"""
                   uuuu ""$$$$$$$$$$uuu
          u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
          $$$$$$$$$$""""           ""$$$$$$$$$$$"
           "$$$$$"                      ""$$$$""
             $$$"                         $$$$ '''
        )
        print("\n" * 2)
        print("You lose!")
        print("The word was: " + word)
    print("Play another game? Press 'n' to quit. Any other key to continue.")
    new_game = input()
    if new_game == "n":
        sys.exit()
