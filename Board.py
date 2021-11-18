# -*- coding: utf-8 -*-

# Create a board by adding Tiles to an array. idk
class Board:
    def __init__(self,board):
        self.board = board
            
        
    def printBoard(self):
        for i in range(9):
            for j in range(9):
                p = self.board[i][j]
                if(p == 0):
                    print(" ",end = "")
                else:
                    print(p,end = "")
            print()
        return -1