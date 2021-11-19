from Board import Board
from CSP_sudoku import CSP

"""

This program reads in 9 characters in the same column then 9 rows,
if file has more characters in the column, program rejects input.

example of accepted file:
    111111111
    222222222
    333333333
    444444444
    555555555
    666666666
    777707777
    888888888
    999999999

"""


def get_board():
    # This piece is for if we want to input a text file via command line
    # UserFile = input("input filename (ex: filename.txt)")
    UserFile = "SodokuBoard.txt"
    f = open(UserFile, "r")
    full = []

    for _ in range(9):
        x = []
        x.extend(f.readline())

        # if "\n" is not in list, program doesn't die
        try:
            x.remove("\n")
        except:
            pass

        if(len(x) != 9):
            raise Exception("Input line is too short")

        # converts from chars to ints
        for i in range(len(x)):
            x[i] = int(x[i])
            if(x[i] < 0 or x[i] > 9):
                raise Exception("An input number is out of domain")
        full.append(x)
    f.close()
    return full

def getBoard(filePath):
    f = open(filePath)
    file = f.readlines()

    f.close()

    return [list(line.strip()) for line in file]

def main():
    # Get path to the text file with a sudoku board
    fileName = 'board1'
    filePath = 'sudokuTestingBoards/{}.txt'.format(fileName)
    board = getBoard(filePath)

    # print(board)
    
    sudoku = Board(board)
    sudoku.printBoard()

    solve = CSP().backtrackSolve(sudoku)
    # print(solve.board)


if __name__ == '__main__':
    main()
