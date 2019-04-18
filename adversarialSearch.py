#!/usr/bin/python3.6

import numpy as np 

INF = 1000
visited = [list()]

def calcPion(currState, turn) -> int :
    num = 0
    for x in currState :
        if x==turn :
            num+=1
    return num

def movePion(currState, currPos)->list:
    possiblePos = list()
    if currPos%3 != 0 and currState[currPos-1] == 0 : # not most-left position
        possiblePos.append(currPos-1)
    if currPos/3 != 0 and currState[currPos-3] == 0 : # not most-top position
        possiblePos.append(currPos-3)
    if currPos%3 != 2 and currState[currPos+1] == 0 : # not most-right position
        possiblePos.append(currPos+1)
    if currPos/3 <2 and currState[currPos+3] == 0 : # not most-bottom position
        possiblePos.append(currPos+3)
    return possiblePos

def addPion(currState)->list :
    possiblePos = list()
    for pos in range(len(currState)):
        if currState[pos] == 0 :
            possiblePos.append(pos)
    return possiblePos

def successors(currState, turn)->list :
    succs = list()
    succ = list()
    # numPion = calcPion(currState, turn)
    # # print(numPion)
    # if numPion==3 :
    #     for currPos in range (len(currState)) :
    #         if currState[currPos] != turn:
    #             continue
    #         possiblePos = movePion(currState, currPos)
    #         for pos in possiblePos :
    #             succ = list(currState)
    #             succ[pos] = turn
    #             succ[currPos] = 0
    #             if succ not in visited :
    #                 visited.append(succ)
    #                 succs.append(succ)
    # elif numPion<3 :
    possiblePos = addPion(currState)
    # print(possiblePos)
    for pos in possiblePos :
        succ = list(currState)
        succ[pos] = turn
        succs.append(succ)
    return succs

def isGoal(state : list, turn : int)->bool :
    goal = [ state[3*x] for x in range(3)]
    if goal == [turn, turn, turn] :
        return True
    goal = [ state[x] for x in range(3)]
    if goal == [turn, turn, turn] :
        return True
    goal = [ state[3*x+1] for x in range(3)]
    if goal == [turn, turn, turn] :
        return True
    goal = [ state[3*x+2] for x in range(3)]
    if goal == [turn, turn, turn] :
        return True
    goal = [ state[4*x] for x in range(3)]
    if goal == [turn, turn, turn] :
        return True
    goal = [ state[2*(x+1)] for x in range(3)]
    if goal == [turn, turn, turn] :
        return True
    return False
    

def maxVal(currState, turn):
    # input()
    if isGoal(currState, turn):
        return [turn, currState]
 
    val = -INF
    optState = list()
    for succ in successors(currState, turn):
        minv = minVal(succ, -turn)[0]
        if val < minv :
            val = minv
            optState = succ
    return [val, optState]

def minVal(currState, turn):
    # input()
    if isGoal(currState, turn):
        return [turn, currState]

    val = INF
    optState = list()
    for succ in successors(currState, turn):
        maxv = maxVal(succ, -turn)[0]
        if val > maxv :
            val = maxv
            optState = succ
    return [val, optState]

def printBoard(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])

def adversarialSearch(initState : list):
    state = initState
    turn = 1
    while not isGoal(state, turn) :   
        xx = maxVal(state, turn)
        state = xx[1]
        cost = xx[0]
        printBoard(state) 
        print(cost, "\n----\n")
        if calcPion(state, 0)>0 :
            x = int(input())
            state[x] = -1
    if isGoal(state, 1):
        print("AI wins")
    elif isGoal(state, -1):
        print("You win")
    else:
        print("Draw")

if __name__ == '__main__' :
    initState = [0,0,0,0,0,0,0,0,0]
    adversarialSearch(initState)
