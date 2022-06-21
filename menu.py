#!/usr/bin/env python3

from simple_term_menu import TerminalMenu

options = ["Add expense", "Edit stable income(Setings)", "Exit"]

mainMenu = TerminalMenu(options, title = "Main menu")
addMenu = TerminalMenu(["Food", "Entertainment", "New category", "Back"], title = "Add expense")
quitting = False

while quitting == False:
    optionsIndex = mainMenu.show()
    optionsChoice = options[optionsIndex]

    if(optionsChoice == "Exit"):
        quitting = True
    if(optionsChoice == "Add expense"):
        addMenu.show()
    else:
        qutting = True
