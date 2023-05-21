tic_tac_board = [
    ["_","_", "_"],
    ["_","_", "_"],
    ["_","_", "_"],
]

def print_board(board):
    for r in board:
        print(*r)

spot = input("Give me a row and colum separated by comma to put an X")
spot = spot.split()

tic_tac_board[int(spot[0])][int(spot[1])] = "X"

spot = input("Give me a row and colum separated by space to put an 0")
spot = spot.split()
print(spot)
tic_tac_board[int(spot[0])][int(spot[1])] = "0"
print_board(tic_tac_board)