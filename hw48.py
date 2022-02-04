
def putInBoard(board: list, instruct: str, side: int):
    row = (int(instruct)-1)//3
    col = (int(instruct)-1) % 3
    #print(row, col)
    if board[row][col] != 0:
        return 0, board
    else:
        board[row][col] = side
        return 1, board


def rowWillWin(row: int, side: int, board: list, non: int):
    if board[row].count(side) != 2:
        return 0, 0
    for i in range(3):
        if board[row][i] == non:
            return 1, i
    return 0, 0


def colWillWin(col: int, side: int, board: list, non: int):
    counter = 0
    for i in range(3):
        if board[i][col] == side:
            counter += 1
    if counter != 2:
        return 0, 0
    for i in range(3):
        if board[i][col] == non:
            return 1, i
    return 0, 0


def slopeWillWin1(side: int, board: list, non: int):
    counter = 0
    for i in range(3):
        if board[i][i] == side:
            counter += 1
    if counter != 2:
        return 0, 0, 0
    for i in range(3):
        if board[i][i] == non:
            return 1, i, i
    return 0, 0, 0


def slopeWillWin2(side: int, board: list, non: int):
    counter = 0
    for i in range(3):
        if board[i][2-i] == side:
            counter += 1
    if counter != 2:
        return 0, 0, 0
    for i in range(3):
        if board[i][2-i] == non:
            return 1, i, (2-i)
    return 0, 0, 0


def targetWillWin(board: list, target: int):
    flag = 0
    for i in range(3):
        flag, col = rowWillWin(i, target, board, 0)
        if flag == 1:
            return 1, i, col
        flag, row = colWillWin(i, target, board, 0)
        if flag == 1:
            return 1, row, i
        flag, row, col = slopeWillWin1(target, board, 0)
        if flag == 1:
            return 1, row, col
        flag, row, col = slopeWillWin2(target, board, 0)
        if flag == 1:
            return 1, row, col

    return 0, 0, 0


def helpWin(board: list):
    target = 0
    if board[1][1] == 0:
        return 1, 1
    for i in range(3):
        flag, col = rowWillWin(i, target, board, 2)
        if flag == 1:
            return 1, i, (col+1) % 3
        flag, row = colWillWin(i, target, board, 2)
        if flag == 1:
            return 1, (row+1) % 3, i
        flag, row, col = slopeWillWin1(target, board, 2)
        if flag == 1:
            return 1, (row+1) % 3, (col+1) % 3
        flag, row, col = slopeWillWin2(target, board, 2)
        if flag == 1:
            return 1, (row+1) % 3, (col+1) % 3


def isWin(board: list):
    for i in range(3):
        if board[i][0] != 0 and board[i][0] == board[i][1] == board[i][2]:
            return 1
        if board[0][i] != 0 and board[0][i] == board[1][i] == board[2][i]:
            return 1
    if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
        return 1
    if board[2][0] != 0 and board[2][0] == board[1][1] == board[0][2]:
        return 1
    return 0


def printBoard(board: list):
    for i in board:
        for j in i:
            print(j, end=' ')
        print()


def isTie(board: list):
    for i in board:
        for j in i:
            if j == 0:
                return 0
    return 1


def process():
    side = int(input())
    #enemy = side % 2 + 1
    error = 0
    whoWin = 0
    undecide = 0
    #print(side, enemy)
    board = [[0 for _ in range(3)] for _ in range(3)]
    # printBoard(board)
    instructs = input().split()
    # print(instructs)
    for instruct in instructs:
        flag, board = putInBoard(board, instruct, side)
        if isWin(board) == 1:
            if side == 1:
                whoWin = 1
            else:
                whoWin = 2
            break
        if flag == 0:
            error = 1
        if flag != 0:
            side = side % 2+1
    if error == 1:
        print('Error')
    else:
        print('OK')
    printBoard(board)
    if whoWin == 1:
        print('Player win')
    elif whoWin == 2:
        print('Computer win')
    else:
        if isTie(board) == 1:
            print('Tie')
        else:
            undecide = 1
            print('Undecided')
    if undecide == 1:
        flag, row, col = targetWillWin(board, 2)
        if flag == 1:
            undecide = 0
            print(row*3+col+1)
    if undecide == 1:
        flag, row, col = targetWillWin(board, 1)
        if flag == 1:
            undecide = 0
            print(row*3+col+1)
    if undecide == 1:
        flag, row, col = helpWin(board)
        if flag == 1:
            print(row*3+col+1)


def test():
    board = [[2, 1, 0], [0, 1, 0], [0, 2, 0]]
    printBoard(board)
    print(targetWillWin(board, 1))
    print(helpWin(board))


# test()
process()
