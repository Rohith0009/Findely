import os
import sys
from turtle import clear
from colorama import init

init()
from colorama import init, Fore as F, Back as B, Style as S

S.R = S.RESET_ALL
F.R = F.RESET
B.R = B.RESET
import Scripts.main as Main
import Scripts.utils as Utils


def default():
    version = "V1 Beta-2"
    Utils.clearConsole()
    print(f"{F.LIGHTYELLOW_EX}Loading Findely @ {version} ...{S.R}")
    print("")
    choice = ""
    word_positions = ""
    print(f"{F.LIGHTBLUE_EX}Welcome To Findely{S.R}")
    print(
        f"{F.LIGHTCYAN_EX}Findely is a app in which you can find words in a sentence{S.R}"
    )
    print(
        f"{F.LIGHTRED_EX}Note: Type X At Any Prompt To Return To The Main Screen and Press Q to quit The app{S.R}"
    )
    Main.main_menu()
