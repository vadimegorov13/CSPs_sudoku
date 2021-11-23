# Returns 2d array of integer numbers that were read from the file
def getBoard(fileName):
    f = open('sudokuTestingBoards/{}.txt'.format(fileName))
    file = f.readlines()
    return [list(map(int, list(line.strip()))) for line in file]
