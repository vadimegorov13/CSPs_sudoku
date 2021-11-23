class Backtrack:
    def __init__(self, board):
        self.board = board
        self.nodes = 0

    # Print sudoku board
    def __str__(self):
        board = ""
        for y in range(9):
            for x in range(9):
                p = self.board[y][x]
                if(p == 0):
                    board += "_ "
                else:
                    board += str(p) + " "
            board += '\n'

        return board

    # Check if variable can be assigned to the tile
    def isLegal(self, y, x, variable):
        # Check if row or column already has this variable
        for i in range(9):
            if self.board[y][i] == variable or self.board[i][x] == variable:
                return False

        # Check if 3x3 box already has this variable
        threeByThreeY = y - (y % 3)
        threeByThreeX = x - (x % 3)
        for i in range(3):
            for j in range(3):
                if self.board[threeByThreeY + i][threeByThreeX + j] == variable:
                    return False
        return True

    # Get index of first empty tile
    def getTileIndex(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    return y, x
        return -1, -1

    # Solve sudoku by using Backtracking
    def solve_sudoku(self):
        # Get location of the tile without variable
        y, x = self.getTileIndex()

        # Check if sudoku is solved
        if y == -1 and x == -1:
            return True

        # Increase node counter
        self.nodes += 1

        # Check if variable is legal
        for variable in range(1, 10):
            if self.isLegal(y, x, variable):
                # Assign variable to the board
                self.board[y][x] = variable

                # Recursion
                if self.solve_sudoku():
                    return True

                # Restart if recursion returns false
                self.board[y][x] = 0

        return False
