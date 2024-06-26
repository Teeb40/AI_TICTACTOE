"""
Tic Tac Toe Player
"""

import math
import time
import copy
from copy import deepcopy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #start with an x value == True
    x = str(board).count(X)
    y = str(board).count(O)
    if x == 0 and y == 0:
        return X
    elif x == y:
        return X
    else: return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    row = 0
    column = -1
    for i in board[0]:
        column +=1
        if i == EMPTY:
            moves.add((row,column))
    row = 1
    column = -1
    for i in board[1]:
        column +=1
        if i == EMPTY:
            moves.add((row,column))
    row = 2
    column = -1
    for i in board[2]:
        column +=1
        if i == EMPTY:
            moves.add((row,column))

        
    return moves
    
    

    
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #check if the action is valid
    if action not in actions(board): 
        raise ValueError
    #find an equivilant value to board
    new_board = []
    row = 0
    column = -1
    row2 = []
    row3 = []
    row4 = []

    for i in board[0]:
        column +=1
        if i == EMPTY and action == (row,column):
            if player(board) == X:
                i = X
            elif player(board) == O:
                i = O
        row2.append(i)
    row = 1
    column = -1
    for i in board[1]:
        column +=1
        if i == EMPTY and action == (row,column):
            if player(board) == X:
                i = X
            elif player(board) == O:
                i = O
        row3.append(i)
    row = 2
    column = -1
    for i in board[2]:
        column +=1
        if i == EMPTY and action == (row,column):
            if player(board) == X:
                i = X
            elif player(board) == O:
                i = O
        row4.append(i)
    new_board = [row2,row3,row4]
    return new_board

    
    

    


    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    X_c = 0
    O_c = 0
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    for i in board[0]:
        if i == X:
            X_c +=1
            if X_c == 3:
                return X
        elif i == O:
            O_c +=1
            if O_c == 3:
                return O
    X_c = 0
    O_c = 0
    for i in board[1]:
        if i == X:
            X_c +=1
            if X_c == 3:
                return X
        elif i == O:
            O_c +=1
            if O_c == 3:
                return O
    X_c = 0
    O_c = 0
    for i in board[2]:
        if i == X:
            X_c +=1
            if X_c == 3:
                return X
        elif i == O:
            O_c +=1
            if O_c == 3:
                return O
    
    if X == row1[0] and X == row2[0] and X == row3[0]:
        return X
    elif X == row1[1] and X == row2[1] and X == row3[1]:
        return X
    elif X == row1[2] and X == row2[2] and X == row3[2]:
        return X
    elif X == row1[0] and X == row2[1] and X == row3[2]:
        return X
    elif X == row1[2] and X == row2[1] and X == row3[0]:
        return X
    elif O == row1[0] and O == row2[1] and O == row3[2]:
        return O
    elif O == row1[2] and O == row2[1] and O == row3[0]:
        return O
    elif O == row1[0] and O == row2[0] and O == row3[0]:
        return O
    elif O == row1[1] and O == row2[1] and O == row3[1]:
        return O
    elif O == row1[2] and O == row2[2] and O == row3[2]:
        return O
    
   

    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    elif actions(board) == set():
        return True
    else:
        return False
    
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif actions(board) == set() and winner(board) != X or winner(board) != O:
        return 0



def minimax(board):
    """
    # Returns the optimal action for the current player on the board.
    # """
    def get_key(val):
        for key, value in move_action_counter.items():
            if val == value:
                return key
    deep_board = deepcopy(board)
    possible_moves = []
    possible_defensive_moves = []
    action_to_get_move = []
    score_for_each_move = {}
    move_and_counter_move = {}
    scores = []
    
    def evaluate(board):
            row1 = board[0]
            row2 = board[1]
            row3 = board[2]
            count = 0
            CountO = 0
            score = 0
            
            if X == row1[0] and X == row2[1] and X == row3[2]:
                score += 30
            elif X == row1[2] and X == row2[1] and X == row3[0]:
                score += 30
            elif O == row1[0] and O == row2[1] and O == row3[2]:
                score -= 30
            elif O == row1[2] and O == row2[1] and O == row3[0]:
                score -= 30
            for i in row1:
                if X == i:
                    count +=1
                    if count == 2:
                        score+=10
                    if count == 1:
                        score += 5
                if O == i:
                    CountO +=1
                    if CountO == 2:
                        score += -10
                    if CountO == 1:
                        score +=-5
         
            for j in row2:
                if X == j:
                    count +=1
                    if count == 2:
                        score+=10
                    if count == 1:
                        score += 5
                if O == j:
                    CountO +=1
                    if CountO == 2:
                        score += -10
                    elif CountO == 1:
                        score +=-5
            
            for k in row3:
                if X == k:
                    count +=1
                    if count == 2:
                        score+=10
                    if count == 1:
                        score += 5
                if O == k:
                    CountO +=1
                    if CountO == 2:
                        score += -10
                    if CountO == 1:
                        score +=-5
            if X == row1[0] and X == row2[0] or row2[0] == X and row3[0] == X:
                score +=10
            if X == row1[1] and X == row2[1] or row2[1] == X and row3[1] == X:
                score +=10
            if X == row1[2] and X == row2[2] or row2[2] == X and row3[2] == X:
                score +=10
            if X == row1[0] and X == row2[1]:
                score +=10
            if X == row1[2] and X == row2[1]:
                score +=10 
            if O == row1[0] and O == row2[1]:
                score -=10
            if O == row1[2] and O == row2[1]:
                score -=10
            if O == row1[0] and O == row2[0] or row2[0] == O and row3[0] == O:
                score -=10
            if O == row1[1] and O == row2[1] or row2[1] == O and row3[1] == O:
                score -=10
            if O == row1[2] and O == row2[2] or row2[2] == O and row3[2] == O:
                score -=10
            
            return score
    
    

    moves = []
    boards_ = []
    move_action = {}
    board_score = {}
    counters = []
    counter_score = {}
    scores_C = []
    scores_B = []
    move_action_counter = {}
    for move in actions(board):
        moves.append(move)
        boards_.append(result(board,move))
        move_action.update({move:result(board,move)})
  
        for boards in boards_:
            # board_score.update({evaluate(counter):boards})
            for action in actions(boards):
                counters.append(result(boards,action))
                
                for counter in counters:
                    counter_score.update({evaluate(counter):counter})
                    move_action_counter.update({action:counter})
                    
                for i in counter_score:
                                
                                scores_C.append(i)
                                for scoring in scores_C:
                                    if scoring > scoring:
                                        scoring = scoring
                                for scoring_les in scores_C:
                                    if scoring < scoring:
                                        scoring_les = scoring
                                if scoring == max(scores_C) and player(board) == X:  
                                    return get_key(counter_score[scoring]) 
                                elif scoring_les == min(scores_C) and player(board) == O:  
                                    return get_key(counter_score[scoring_les]) 
                                
            

print(minimax([[EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY]]))
# print(result([[EMPTY, X, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]],(0,0)))
