from copy import deepcopy
from os import system
import sys
from time import perf_counter

from Backtrack_sudoku import Backtrack
from Board import getBoard
from CSP_sudoku import CSP


# Write table to the file
def log_table(list_to_print):
    original_stdout = sys.stdout
    with open("test_table.txt", "w") as f:
        sys.stdout = f
        cool_table_print(list_to_print)
        sys.stdout = original_stdout

# Print boards
def print_boards(initial_board, solved_board):
    print("-----------+-----------" + "----+----" +
          "-----------+---------------")
    print("        Initial Board  " + "    |   " + "   Solved Board")
    print("-----------------------" + "----+----" +
          "---------------------------")

    for y in range(9):
        print("      ", end="")
        for x in range(9):
            ib = initial_board.board[y][x]
            if(ib == 0):
                print("_ ", end="")
            else:
                print(str(ib) + " ", end="")

        print("   |    ", end="")

        for x in range(9):
            sb = solved_board.board[y][x]
            if(sb == 0):
                print("_ ", end="")
            else:
                print(str(sb) + " ", end="")

        print()
    print()

# Print table
def cool_table_print(list_to_print):
    # Clear terminal and print table again with new values
    system("clear")  # You can remove this line if you want
    print("\n{:<10} {:<15} {:<15} {:<15}".format(
        'Sudoku', '| Algorithm', '| Time', '| Opened Nodes'))
    print("{:<10} {:<15} {:<15} {:<15}".format(
        'level', '| name', '| seconds', '| #'))

    for l in list_to_print:
        print("-----------+---------------+---------------+---------------")
        print("{:<10} {:<15} {:<15} {:<15}".format(
            l["fl"], "| " + l["a"], "| " + str(round(l["t"], 10)), "| " + str(l["on"])))
        print_boards(l["ib"], l["sb"])


def test():
    filenames = ["easy", "medium", "hard", "expert", "evil"]
    algorithms = [CSP, Backtrack]
    list_to_print = list()

    # Execute each algorithm on each graph 5 times
    for filename in filenames:
        for algorithm in algorithms:
            # Get board
            board = getBoard(filename)
            solver = algorithm(deepcopy(board))

            initial_board = deepcopy(solver)

            # Start timer
            start_t = perf_counter()
            # Execute algorithm;
            solver.solve_sudoku()
            stop_t = perf_counter()

            # Append result to the list
            list_to_print.append({"on": solver.nodes, "fl": filename, "a": algorithm.__name__,
                                 "t": stop_t - start_t, "ib": deepcopy(initial_board), "sb": deepcopy(solver)})
    # Print cool table
    cool_table_print(list_to_print)
    # Write table to the txt file
    # log_table(list_to_print)
