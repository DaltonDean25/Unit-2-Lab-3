#Dalton Dean
#Unit 2 Lab 3
#TicTacToe made with a class 

#Imports
from tic_tac_toe import *
from os import system as s
from random import randint
from time import sleep
#Global
game = TicTacToe()




def selectTokens(): #Allows player to choice their symbol, and sets the computers symbol
    while True:
      pToken = input("Choose which token you'll play with (X or O)\n> ").upper()
      if pToken in ["X", "x", "O", "o"]:
        break
      s('clear'), print("Invalid choice...\n\n")

  
    if pToken == "X":
      cToken = "O"
    else:
      cToken = "X"

    return pToken, cToken
      

def cTurn(token): #Computer randomly selects a row and column to play their token into
    invalid = True
    while invalid:
      row = randint(0,2)
      index = randint(0,2)
      invalid = game.place_token(token, row, index)


def pTurn(token): #Checks player input for row and column to play in and plays it too
    invalid = True
    error = ""

    while invalid:
      try:
        s('clear')
        print(f"{game}\n\n{error}\n")

        row = int(input("Which ROW would you like to play into... (1, 2, 3)\n> "))
        column = int(input("\nWhich COLUMN would you like to play into...(1, 2, 3)\n> "))

        if row in [1, 2, 3] and column in [1, 2, 3]:
          invalid = game.place_token(token, row-1, column-1)
          if invalid:
            error = "!> Position taken..."
        else:
          error = "!> Position not in range..."
      except:
        error = "!> Integers only..."


def main():
    s('clear')
    pToken, cToken = selectTokens()
    spaces = 9
    winner = None
    playing = True
    
    
    while playing:
      cTurn(cToken)
      pTurn(pToken)
      spaces -= 2

      playing, winner = game.is_winner()
      if not playing or spaces <= 0:
        break
    
    
    s('clear'), print(game)
    if winner == pToken:
      print("You won! Congrats!")
    elif winner == cToken:
      print("You lost... better luck next time")
    else:
      print("You tied...")


if __name__ == "__main__":
    main()

