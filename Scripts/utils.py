import os
import Scripts.main as Main


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def return_main():
    clearConsole()
    Main.main_menu()
