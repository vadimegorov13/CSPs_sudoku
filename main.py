from CSP_sudoku import CSP
from Backtrack_sudoku import Backtrack
from time import time
from copy import deepcopy

# Returns 2d array of integer numbers that were read from the file
def getBoard(fileName):
    f = open('sudokuTestingBoards/{}.txt'.format(fileName))
    file = f.readlines()
    return [list(map(int, list(line.strip()))) for line in file]


def main():
    # Get path to the text file with a sudoku board
    fileName = 'expert'
    board = getBoard(fileName)

    # Solve sudoku by using CSP
    csp_solver = CSP(deepcopy(board))
    print("This is the original board: {}.txt\n".format(fileName))
    print(csp_solver)
    print("\n\n")
    start = time()
    csp_solver.CSPsudoku()
    end = time()

    print("This is solved with CSP solver:\n")
    print(csp_solver)
    print("Nodes opened: {}".format(csp_solver.nodes))
    print("Time: {}\n".format(end - start))

    # Solve sudoku by using Backtracking
    backtrack_solver = Backtrack(deepcopy(board))
    start = time()
    backtrack_solver.BacktrackSudoku()
    end = time()

    print("This is solved with backtracking:\n")
    print(backtrack_solver)
    print("Nodes opened: {}".format(backtrack_solver.nodes))
    print("Time: {}\n".format(end - start))


if __name__ == '__main__':
    main()
