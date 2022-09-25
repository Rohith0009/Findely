import Scripts.utils as Utils
import os
import sys
from turtle import clear
from colorama import init

init()
from colorama import init, Fore as F, Back as B, Style as S

S.R = S.RESET_ALL
F.R = F.RESET
B.R = B.RESET
var_again = ""


def complex():
    def checking_2():
        sentence = input(f"{F.LIGHTMAGENTA_EX}Type Your Sentence Here: {S.R}").lower()
        if sentence == "x":
            Utils.return_main()
        elif sentence == "q":
            sys.exit()
        elif sentence == "":
            print(f"{F.LIGHTRED_EX}Invalid Response. You Need To Type Something{S.R}")
            complex()
        word = input(f"{F.LIGHTMAGENTA_EX}Type The Word which you want to find: {S.R}")
        check_word = word.lower()
        if check_word == "x":
            sys.exit()
            print("")
        elif check_word == "q":
            sys.exit()
        elif check_word == "":
            print(f"{F.LIGHTRED_EX}Invalid Response. You Need To Type Something{S.R}")
            complex()
        elif len(check_word) == 1:
            print(f"{F.LIGHTRED_EX}The Word Has To be At least Two Letter{S.R}")
            complex()
        value = check_word in sentence
        if value:
            occurrence = sentence.count(check_word)
            print(
                f"{F.LIGHTGREEN_EX}{word} Was Found In The Sentence {occurrence} Times.{S.R}"
            )
            i = 1
            word_positions = "The"
            while i <= occurrence:
                word_position = sentence.split()
                word_position = word_position.index(check_word) + 1
                word_positions = word_positions + ", " + str(word_position)
                sentence = sentence.replace(word, "*/", 1)
                i = i + 1
            print(f"{F.LIGHTGREEN_EX}It Is {word_positions} Word{S.R}")
            print("")

        else:
            print(f"{F.LIGHTRED_EX}{word} was not found in the sentence{S.R}")
            print("")

    checking_2()

    def again():
        var_again = input(
            f"{F.LIGHTYELLOW_EX}Do you want to run again?({F.GREEN}y{S.R}/{F.LIGHTRED_EX}n{S.R}) {S.R}"
        ).lower()
        if var_again == "x":
            Utils.return_main()
        print("")

        if var_again == "y":
            checking_2()
        elif var_again == "n":
            sys.exit()
        else:
            print(f"{F.LIGHTRED_EX}Invalid Response. Respond With Y or N.{S.R}")
            again()

    while var_again < "y":
        again()
