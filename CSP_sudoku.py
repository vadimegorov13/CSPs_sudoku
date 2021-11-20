from copy import deepcopy


class CSP:
    def __init__(self, board):
        self.board = board
        self.unassigned_vars = self.getUnassignedVariables()
        self.nodes = 0

    # Print sudoku board
    def __str__(self):
        board = ""
        for y in range(9):
            for x in range(9):
                p = self.board[y][x]
                if(p == 0):
                    board += "0 "
                else:
                    board += str(p) + " "
            board += '\n'

        return board

    # Get domain of the tile
    # Constaints thing is happening here
    def getDomain(self, y, x, board):
        # Init domain list
        domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Remove variable from the domain if row already has this variable
        for i in range(9):
            if board[y][i] != 0:
                if board[y][i] in domain:
                    domain.remove(board[y][i])

        # Remove variable from the domain if column already has this variable
        for i in range(9):
            if board[i][x] != 0:
                if board[i][x] in domain:
                    domain.remove(board[i][x])

        # Remove variable from the domain if 3x3 box already has this variable
        threeByThreeY = y - y % 3
        threeByThreeX = x - x % 3
        for i in range(3):
            for j in range(3):
                if board[threeByThreeY+i][threeByThreeX+j] != 0:
                    if board[threeByThreeY+i][threeByThreeX+j] in domain:
                        domain.remove(board[threeByThreeY+i][threeByThreeX+j])

        # Return domain of the tile
        return domain

    # Get domains of unassigned variables
    def getUnassignedVariables(self):
        unassigned_variables = list()
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    unassigned_variables.append(
                        self.getDomain(y, x, self.board))
                else:
                    # append 10 if a tile already has variable
                    unassigned_variables.append([10])

        return unassigned_variables

    # Get the length of domain of the tile
    # Helper function of the getTileIndex
    def getDomainLength(self, domain):
        # If tile already has a variable return 10 so that heuristic
        # can ignore it basically
        # else return length of the domain
        if 10 in domain:
            return 10
        else:
            return len(domain)

    # Return indexs of the tile with the smallest domain length
    def getTileIndex(self):
        domains = list()

        # Get domain length of a unsigned tiles
        for domain in self.unassigned_vars:
            domains.append(self.getDomainLength(domain))

        # Get the tile with the smallest domain
        min_domain = min(domains)

        # If tile's domain is empty (already has a variable assigned)
        # which means that puzzle is solved
        # return -1 -1 indexes so we can kill recursing
        if min_domain == 10:
            return -1, -1

        # Get y and x indexes of the tile
        y = domains.index(min_domain) // 9
        x = domains.index(min_domain) % 9

        return y, x

    # Solve sudoku by using CSP
    def CSPsudoku(self):
        # Get location of the tile with the smallest domain length
        y, x = self.getTileIndex()

        # Check if sudoku is solved
        if y == -1 and x == -1:
            return True

        # Increase node counter
        self.nodes += 1

        # Check if variable suits the constraints
        for variable in self.unassigned_vars[y*9 + x]:
            # Assign variable to the board
            self.board[y][x] = variable

            # Copy unassigned_vars in case recursion return false
            unassigned_vars_copy = deepcopy(self.unassigned_vars)

            # Update unassigned_vars, basically remove the tile to
            # which we assignd a variable from the unassigned_vars
            self.unassigned_vars = self.getUnassignedVariables()

            # Recursion
            if self.CSPsudoku():
                return True

            # If recursion returned false assign 0 to the index of
            # current tile
            self.board[y][x] = 0

            # Restart the unassigned_vars
            self.unassigned_vars = unassigned_vars_copy

        # Return false if nothing fits
        return False
