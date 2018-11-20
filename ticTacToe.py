#Michelle Montevago
#Intro To Programming
#November 18th 2018

global board
symbol = ["  ", "x", "o"]

def printRow(row):
    output = "|"
    for cell in row:
        output += " " + symbol[cell] + " |"
    print(output)

def print(board):
    for i in range (0,3):
        print ("+___________+")
        printRow(board[i])
    print("+__________+")

def markBoard(board, row, col, player):
    if board [row][col] == 0:
        board [row][col] = player
    else:
        print("Pick a different spot")
        getPlayerMove()
        return False

def getPlayerMove():
    row,col = input ("Please enter a row and column").split(" , ")
    return (int(row), int(col))

def hasBlanks(board):
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == 0:
                return True
    return False

def main ():
    player = 1
    board = [[0,0,0], [0,0,0], [0,0,0]]
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1

main()
            
