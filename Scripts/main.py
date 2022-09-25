import os
import sys
from turtle import clear
from colorama import init
import Scripts.simple as Simple
import Scripts.complex as Complex

init()
from colorama import init, Fore as F, Back as B, Style as S

S.R = S.RESET_ALL
F.R = F.RESET
B.R = B.RESET


def main_menu():
    print(
        f"""
{F.LIGHTGREEN_EX}1. Simple Mode: Just Checks If The Word Is Present or not.{S.R}
{F.CYAN}2. Complex Mode: Complex Gives Detailed information Like Time Repeated, Where it is located and more.{S.R} {F.LIGHTRED_EX}(Beta){S.R}
  """
    )
    choice = input(f"{F.LIGHTYELLOW_EX}Choice(1-2): {S.R}").lower()
    if choice == "1":
        Simple.simple()
    elif choice == "2":
        Complex.complex()
    elif choice == "q":
        sys.exit()
    elif choice == "":
        print("")
        print(f"{F.LIGHTRED_EX}Invalid Response. You Have To Type Something.{S.R}")
        main_menu()
    else:
        print("")
        print(f"{F.LIGHTRED_EX}Invalid Response. Respond With 1 or 2.{S.R}")
        main_menu()
