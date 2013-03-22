'''
Created on Mar 17, 2013

@author: jeremiahoconnor
'''
import sys
from copy import deepcopy
import gameplay

##
#The board will be represented as a list of list of strings (that is, a 2D array of strings).
# Each string will be "B" for black, "W" for white, or "." for an empty square.

#color is either the string "B" or the string "W", representing the color to play
#time is the time left on your tournament clock (in seconds).


def opponent(x):
    """ Given a string representing a color (must be either "B" or "W"),
        return the opposing color """ 
    if x == "b" or x == "B":
        return "W"
    elif x == "w" or x == "W":
        return "B"
    else:
        return "."


table=[[20,5,5,5,5,5,5,20],[5,1,1,1,1,1,1,5], [5,1,1,1,1,1,1,5],[5,1,1,1,1,1,1,5], [5,1,1,1,1,1,1,5],[5,1,1,1,1,1,1,5], [5,1,1,1,1,1,1,5],[20,5,5,5,5,5,5,20]]


def eval_f(board):
    global table
    eval_f = 0
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem == "W":
                eval_f = eval_f + table[i][j]
            elif elem == "B":
                eval_f = eval_f - table[i][j]
    return eval_f

def bulk_func (state, color, limit, reversed, alpha= -sys.maxint, beta= sys.maxint):
    moves = []
    for i in range(8):
        for j in range(8):
            if gameplay.valid(state, color, (i,j)):
                moves.append((i,j))
    if len(moves) == 0:
        if  limit ==0:
            return "pass", eval_f(state)
        else:
            return "pass", bulk_func(state, opponent(color), limit-1, reversed)[1]
    else:
    
        best = None
        bestMove= moves[0]
        for move in moves:
            newState = deepcopy(state)
            gameplay.doMove(newState,color,move)
            if  limit ==0:
                poss_val= move, eval_f(newState)
            else:
                poss_val= bulk_func(newState, opponent(color), limit-1, reversed, alpha, beta)
            if best == None or betterThan(poss_val[1], best, color, reversed):
                bestMove = move
                best = poss_val[1]
            
            if color == "W" and reversed:
                if best <= alpha:
                    return bestMove, best
                beta = min (beta,best)
                
            if color == "W" and not reversed:
                if best >= beta:
                    return bestMove, best
                alpha = max(alpha,best)
               
            if color == "B" and not reversed:
                if best <= alpha:
                    return bestMove, best
                beta = min (beta,best)
            
            if color == "B" and reversed:
                if best >= beta:
                    return bestMove, best
                alpha = max(alpha,best)
                
        return bestMove, best

def nextMove (board, color, time):
    return bulk_func(board, color, 5, False)[0]
 
def betterThan(val1, val2, color, reversed):
    if color == "W":
        retVal = val1 > val2
    else:
        retVal =  val2 > val1
    if reversed:
        return not retVal
    else:
        return retVal

def nextMoveR(board, color, time):
    return bulk_func(board, color, 5, True)[0]
    