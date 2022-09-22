version=0.1

from colorama import init
init()
from colorama import init, Fore as F, Back as B, Style as S

S.R = S.RESET_ALL
F.R = F.RESET
B.R = B.RESET

print(f"{F.LIGHTYELLOW_EX}Loading Findely @ {version} ...{S.R}")
print("")
var_again = ""
print(f"{F.LIGHTBLUE_EX}Welcome To Findely{S.R}")
print(f"{F.LIGHTCYAN_EX}Findely is a app in which you can find words in a sentence{S.R}")
print("")
def checking():
    sentence = input(f"{F.LIGHTMAGENTA_EX}Type Your Sentence Here: {S.R}")
    word = input(f"{F.LIGHTMAGENTA_EX}Type The Word which you want to find: {S.R}")
    print("")
    value = word in sentence
    if value:
      print(f"{F.LIGHTGREEN_EX}{word} was found in the sentence{S.R}")
      print("")
    else:
      print(f"{F.RED}{word} was not found in the sentence{S.R}")
      print("")

checking()

def again():
    var_again = input (f"{F.LIGHTYELLOW_EX}Do you want to run again?({F.GREEN}y{S.R}/{F.RED}n{S.R}) {S.R}")
    print("")

    if var_again == "y":
        checking()
    elif var_again == "n":
        exit()
    else:
      print(f"{F.RED}Invalid Response. Respond With Y or N.{S.R}")
      again()    

while var_again < "y":
    again()
