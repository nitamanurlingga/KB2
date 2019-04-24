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
    print (board, row, col)
    if board[row][col] != mm.blank :
        return render(request,'tictactoe/tictactoe.html', context) 
    board[row][col] = mm.opponent
    if mm.isGoal(board, mm.opponent) :
        msg = 'You Win!'
    if mm.calcPion(board, mm.blank) == 0:
        msg = 'Draw'
    else :
        [row, col] = mm.findBestPos(board, mm.player)
        board[row][col] = mm.player
        if mm.isGoal(board, mm.player):
            msg = ' You Lose'
    context = {
        'row1' : board[0],
        'row2' : board[1],
        'row3' : board[2],
        'msg'  : msg,
    }   
    return render(request, 'tictactoe/tictactoe.html', context)
