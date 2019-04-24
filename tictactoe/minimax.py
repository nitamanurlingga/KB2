# CONSTS
INF = 1000
ROW = 3
COL = 3
blank = '-'
player = 'o'
opponent = 'x'

def calcPion(board : list, pion : str)->int :
    num = 0
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == pion :
                num+=1
    return num

def isGoal(board : list, pion : str) -> bool :
    for row in range(ROW) :
        if [board[row][x] for x in range(COL)] == [pion, pion, pion] :
            return True
    for col in range(COL) :
        if [board[x][col] for x in range(ROW)] == [pion, pion, pion] :
            return True
    if [board[x][x] for x in range(ROW)] == [pion, pion, pion] :
        return True
    if [board[0][2], board[1][1], board[2][0]] == [pion, pion, pion] :
        return True
    return False
    
def findPossibleMoves(board : list) -> list :
    moves = list()
    for row in range(ROW) :
        for col in range(COL):
            if board[row][col] == blank :
                moves.append([row, col])
    return moves

def maxVal(board : list) -> int :
    if isGoal(board, player) :
        return 10
    if isGoal(board, opponent) :
        return -10
    if calcPion(board, blank) == 0 :
        return 0
    best = -INF
    for [row, col] in findPossibleMoves(board):
        board[row][col] = player
        best = max(best, minVal(board))
        board[row][col] = blank
    return best
    
def minVal(board : list) -> int :
    if isGoal(board, player) :
        return 10
    if isGoal(board, opponent) :
        return -10
    if calcPion(board, blank) == 0 :
        return 0
    best = INF
    for [row, col] in findPossibleMoves(board):
        board[row][col] = opponent
        best = min(best, maxVal(board))
        board[row][col] = blank
    return best
    
def findBestPos(board : list, pion : str) -> list :
    best = -INF
    bestMove = [-1,-1]
    for [row, col] in findPossibleMoves(board):
        board[row][col] = pion
        val = minVal(board)
        if best < val :
            best = val
            bestMove = [row, col]
        board[row][col] = blank
    print('Best cost : ', best)
    return bestMove

def printBoard(board : list):
    for row in range(ROW) :
        print(board[row])

def initBoard():
    board = [ [blank for col in range(COL)] for row in range(ROW) ]
    return board.copy()



