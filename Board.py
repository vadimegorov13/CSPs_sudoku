from Tile import Tile
DEF_BOARD = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Create a board by adding Tiles to an array. idk
class Board:
    def __init__(self, board=DEF_BOARD):
        self.board = self.createBoard(board)

    def createBoard(self, board):
        for y in range(9):
            for x in range(9):
                board[y][x] = Tile(board[y][x])

        return board

    def isComplete(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x].variable == 0:
                    return False
        return True

    # Print dat shit

    def printBoard(self):
        for i in range(9):
            for j in range(9):
                p = self.board[i][j].variable
                if(p == 0):
                    print("_", end=" ")
                else:
                    print(p, end=" ")
            print()
        return -1
