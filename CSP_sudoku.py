#  check constraints
#  and other stuff idk
#  somehow its going to recurse through every tile and so on idk

class CSP:
    def passesConstraints(self, board, tile, value):
        return True

    def getTile(self, board):
        for y in range(9):
            for x in range(9):
                # print(board[x][y].variable)
                if board[x][y].variable == 0:
                    return board[x][y]

    def backtrackSolve(self, board):
        if (board.isComplete()):
            return board

        tile = self.getTile(board.board)
        # print(variable)

        for value in tile.domain:
            if self.passesConstraints(board, tile, value):
                board.setTile(tile, value)

                result = self.backtrackSolve(board)

                if not result:
                    return result

                board.removeTile(tile, value)

        return False