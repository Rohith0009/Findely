#Head
version="1 Beta-1"
import os
import sys
from turtle import clear
from colorama import init
init()
from colorama import init, Fore as F, Back as B, Style as S
S.R = S.RESET_ALL
F.R = F.RESET
B.R = B.RESET
print(f"{F.LIGHTYELLOW_EX}Loading Findely @ {version} ...{S.R}")
print("")
var_again = ""
choice=""
word_positions = ""
print(f"{F.LIGHTBLUE_EX}Welcome To Findely{S.R}")
print(f"{F.LIGHTCYAN_EX}Findely is a app in which you can find words in a sentence{S.R}")
print(f"{F.LIGHTRED_EX}Note: Type X At Any Prompt To Return To The Main Screen and Press Q to quit The app{S.R}")

#Functions

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#-------------------------------------------------------------------------------------------------------------

def main_menu():
  print(f'''
{F.LIGHTGREEN_EX}1. Simple Mode: Just Checks If The Word Is Present or not.{S.R}
{F.CYAN}2. Complex Mode: Complex Gives Detailed information Like Time Repeated, Where it is located and more.{S.R} {F.LIGHTRED_EX}(Beta){S.R}
  ''')
  choice = input(f"{F.LIGHTYELLOW_EX}Choice(1-2): {S.R}").lower()
  if choice == "1":
    simple()
  elif choice == "2":
    complex()
  elif choice ==  "q": 
    sys.exit()
  else:
    print("")
    print(f"{F.LIGHTRED_EX}Invalid Response. Respond With 1 or 2.{S.R}")
    main_menu() 

#-------------------------------------------------------------------------------------------------------------

def return_main():
  clearConsole()
  main_menu()

#-------------------------------------------------------------------------------------------------------------

def simple():
  def checking():
      sentence = input(f"{F.LIGHTMAGENTA_EX}Type Your Sentence Here: {S.R}").lower()
      if sentence == "x":
        return_main()
      elif sentence == "q":
        sys.exit()  
      elif sentence == "":
        print(f"{F.LIGHTRED_EX}Invalid Response. You Need To Type Something{S.R}")
        simple()
      word = input(f"{F.LIGHTMAGENTA_EX}Type The Word which you want to find: {S.R}")
      check_word = word.lower()
      if check_word == "x":
        sys.exit()
        print("")
      elif check_word == "q":
        sys.exit()
      elif check_word == "":
        print(f"{F.LIGHTRED_EX}Invalid Response. You Need To Type Something{S.R}")
        simple()
      elif len(check_word) == 1:
        print(f"{F.LIGHTRED_EX}The Word Has To be At least Two Letter{S.R}")
        simple()
      value = check_word in sentence
      if value:
        print(f"{F.LIGHTGREEN_EX}{word} was found in the sentence{S.R}")
        print("")
      else:
        print(f"{F.LIGHTRED_EX}{word} was not found in the sentence{S.R}")
        print("")

  checking()

  def again():
      var_again = input (f"{F.LIGHTYELLOW_EX}Do you want to run again?({F.GREEN}y{S.R}/{F.LIGHTRED_EX}n{S.R}) {S.R}").lower()
      if var_again == "x":
        return_main()
      print("")

      if var_again == "y":
          checking()
      elif var_again == "n":
          sys.exit()
      else:
        print(f"{F.LIGHTRED_EX}Invalid Response. Respond With Y or N.{S.R}")
        again()    

  while var_again < "y":
      again()

#-------------------------------------------------------------------------------------------------------------

def complex():
  def checking_2():
    sentence = input(f"{F.LIGHTMAGENTA_EX}Type Your Sentence Here: {S.R}").lower()
    if sentence == "x":
        return_main()
    elif sentence == "q":
        sys.exit()  
    elif sentence == "":
        print(f"{F.LIGHTRED_EX}Invalid Response. You Need To Type Something{S.R}")
        simple()
    word = input(f"{F.LIGHTMAGENTA_EX}Type The Word which you want to find: {S.R}")
    check_word = word.lower()
    if check_word == "x":
        sys.exit()
        print("")
    elif check_word == "q":
        sys.exit()
    elif check_word == "":
        print(f"{F.LIGHTRED_EX}Invalid Response. You Need To Type Something{S.R}")
        simple()
    elif len(check_word) == 1:
        print(f"{F.LIGHTRED_EX}The Word Has To be At least Two Letter{S.R}")
        simple()
    value = check_word in sentence
    if value:
        occurrence = sentence.count(check_word)
        print(f"{F.LIGHTGREEN_EX}{word} Was Found In The Sentence {occurrence} Times.{S.R}")
        i = 1
        word_positions = "The"
        while i <= occurrence:
          word_position = sentence.split()
          word_position = word_position.index(check_word)+1
          word_positions = word_positions+", "+str(word_position)
          sentence = sentence.replace(word, "*/", 1)
          i = i+1
        print(f"{F.LIGHTGREEN_EX}It Is {word_positions} Word{S.R}")
        print("")
  
    else:
        print(f"{F.LIGHTRED_EX}{word} was not found in the sentence{S.R}")
        print("")
  checking_2()
  def again():
      var_again = input (f"{F.LIGHTYELLOW_EX}Do you want to run again?({F.GREEN}y{S.R}/{F.LIGHTRED_EX}n{S.R}) {S.R}").lower()
      if var_again == "x":
        return_main()
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
#Main 

main_menu()
