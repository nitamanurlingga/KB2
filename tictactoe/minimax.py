# CONSTS
INF = 1000
ROW = 3
COL = 3
blank = '-'
player = 'o'
opponent = 'x'

def calcPion(board : list, pion : str)->int :   # menghitung jumlah suatu pion dalam board
    num = 0
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == pion :
                num+=1
    return num

def isGoal(board : list, pion : str) -> bool :  # mengecek apakah pion mencapai goal
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
    
def findPossibleMoves(board : list) -> list :   # mencari seluruh kemungkinan langkah selanjutnya
    moves = list()
    for row in range(ROW) :                     # untuk setiap baris
        for col in range(COL):                  # untuk setiap kolom pada baris
            if board[row][col] == blank :       # jika kotak kosong, maka :
                moves.append([row, col])        # tambahkan kotak ke list kemungkinan langkah selanjutnya
    return moves

def maxVal(board : list) -> int :               # mencari nilai maksimum dari seluruh successor
    if isGoal(board, player) :                  # jika player menang (AI)
        return 10                               # 10 = AI menang
    if isGoal(board, opponent) :                # jika opponent menang (HUMAN)
        return -10                              # -10 = Human menang
    if calcPion(board, blank) == 0 :            # jika tidak ada kotak kosong
        return 0                                # 0 = draw
    best = -INF
    for [row, col] in findPossibleMoves(board):     # untuk setiap kotak yang mungkin untuk langkah selanjutnya
        board[row][col] = player                    # isi kotak kosong dengan player (AI)
        best = max(best, minVal(board))             # update best dengan nilai maksimum
        board[row][col] = blank                     # reset kotak (mengkosongkan kembali)
    return best
    
def minVal(board : list) -> int :               # mencari nilai maksimum dari seluruh successor
    if isGoal(board, player) :                  # jika player menang (AI)
        return 10                               # 10 = AI menang
    if isGoal(board, opponent) :                # jika opponent menang (HUMAN)
        return -10                              # -10 = AI kalah
    if calcPion(board, blank) == 0 :            # jika tidak ada kotak kosong
        return 0                                # 0 = draw
    best = INF
    for [row, col] in findPossibleMoves(board):     # untuk setiap kotak yang mungkin untuk langkah selanjutnya
        board[row][col] = opponent                  # isi kotak kosong dengan opponent (Human)
        best = min(best, maxVal(board))             # update best dengan nilai minimum
        board[row][col] = blank                     # reset kotak (mengkosongkan kembali)
    return best
    
def findBestPos(board : list, pion : str) -> list :     # mengembalikan posisi terbaik untuk langkah yang harus diambil
    best = -INF
    bestMove = [-1,-1]
    for [row, col] in findPossibleMoves(board):         # untuk setiap kemungkinan
        board[row][col] = pion                          
        val = minVal(board)                             # cari nilai dari objective function setiap kemungkinan
        if best < val :
            best = val                                  # best = maksimum 
            bestMove = [row, col]                       # bestMove = posisi dengan nilai objective maksimum
        board[row][col] = blank
    print('Best cost : ', best)
    return bestMove




