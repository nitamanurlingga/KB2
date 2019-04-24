from django.shortcuts import render
from django.http import HttpResponse
from tictactoe import minimax as mm
# Create your views here.

board = [ [mm.blank for col in range(mm.COL)] for row in range(mm.ROW) ]

def index(request):
    return render(request, 'tictactoe/gui.html')

def play(request):
    
    for row in range(mm.ROW):
        for col in range(mm.COL):
            board[row][col] = mm.blank
    context = {
        'row1' : board[0],
        'row2' : board[1],
        'row3' : board[2],
    }
    return render(request, 'tictactoe/tictactoe.html', context)

def klik(request, id):
    msg = str()
    context = {
        'row1' : board[0],
        'row2' : board[1],
        'row3' : board[2],
    }
    col = id%3
    if id<3 :
        row = 0
    elif id < 6:
        row = 1
    else :
        row = 2
    if board[row][col] != mm.blank :                                    # jika kotak yang diklik tidak kosong
        return render(request,'tictactoe/tictactoe.html', context)      # tidak melakukan apa apa, mengembalikan current state
    board[row][col] = mm.opponent                                       # set kotak = opponent (Human)
    if mm.isGoal(board, mm.opponent) :                                  # jika opponent menang
        msg = 'You Win!'
    if mm.calcPion(board, mm.blank) == 0:                               # jika board penuh
        msg = 'Draw'                                                    # draw
    else :
        [row, col] = mm.findBestPos(board, mm.player)                   # cari posisi terbaik untuk langkah selanjutnya
        board[row][col] = mm.player                                     # letakkan player pada posisi terbaik
        if mm.isGoal(board, mm.player):                                 # jika player menang
            msg = ' You Lose'
    context = {                                                         # set data yang dipassing ke view
        'row1' : board[0],
        'row2' : board[1],
        'row3' : board[2],
        'msg'  : msg,
    }   
    return render(request, 'tictactoe/tictactoe.html', context)
