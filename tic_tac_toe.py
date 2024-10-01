import random as r

class TicTacToe:


    #Initalize
    def __init__(self): #TicTacToe attributes
        self.__board = [[" ", " ", " "] for x in range(0,3)]
        self.__turn = r.choice(["X", "O"])


    #Encapsulated Method
    def __check_win(self): #checks if either X or O has reached a win condition    
        #Create a list of just the columns
        columns = [[] for x in range(0,3)]
        for r in self.__board:
          for i in range(0, len(r)):
            columns[i].append(r[i])

        #Create a list of just the diagonals
        diagonals = [[] for x in range(0,2)]
        for i, r in enumerate(self.__board):
          diagonals[0].append(r[i])
          diagonals[1].append(r[-1-i])
        
        #Check all win types
        for type in (self.__board, columns, diagonals):
          for r in type:
            if len(set(r)) == 1 and r[0] != " ":
              return False, r[0]
        

        return True, None
        

    #Regular Methods
    def place_token(self, token, row, index): #places either X or O tokens on the gameboard
        if token == self.__turn:
          if self.__board[row][index] == " ":
            self.__board[row][index] = token
          else:
            return True

          if self.__turn == "X":
            self.__turn = "O"
          else:
            self.__turn = "X"
          return False
        

    def is_winner(self): #returns either X or O as the game winner
        flag, winner = self.__check_win()
        
        return flag, winner
        

    #Magic Methods
    def __str__(self): #displays the game board
        strBoard = "  1 2 3\n"
        for index ,r in enumerate(self.__board):
          for i in range(0, len(r)):
            if i%2 != 0:
              strBoard += r[i] + "|"
            elif i == 0:
              strBoard += f"{str(index+1)} " + r[i] + "|"
            else:
              strBoard += r[i] + "\n"
        return strBoard

  
