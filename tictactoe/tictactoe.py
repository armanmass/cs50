"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_cnt, o_cnt = 0, 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                x_cnt += 1
            if board[i][j] == O:
                o_cnt += 1

    if x_cnt == o_cnt:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set() 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action[0], action[1]

    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("Invalid Move")
    if board[i][j] != EMPTY:
        raise Exception("Invalid Move")

    turn = player(board)

    new_board = copy.deepcopy(board)
    new_board[i][j] = turn

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check row winner
    for i in range(3):
        if board[i][0] == EMPTY: continue
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # check col winner
    for i in range(3):
        if board[0][i] == EMPTY: continue
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
            
    # check diag winner
    if board[1][1] != EMPTY:
        if (board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]):
            return board[1][1]

    return None        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champion = winner(board)
    print("champion: ", champion)
    if champion == X:
        return 1

    if champion == O:
        return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    turn = player(board)
    move = None

    if turn == X:
        best_score = -1e9
        for action in actions(board):
            score = minimax_helper(result(board, action), O, -1e9, 1e9)
            if score > best_score:
                best_score = score
                move = action
    else:
        best_score = 1e9
        for action in actions(board):
            score = minimax_helper(result(board, action), X, -1e9, 1e9)
            if score < best_score:
                best_score = score
                move = action

    return move


def minimax_helper(board, turn, alpha, beta):
    if terminal(board): return utility(board)

    if turn == X:
        max_eval = -1e9
        for action in actions(board):
            eval = minimax_helper(result(board, action), O, alpha, beta) 
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = 1e9
        for action in actions(board):
            eval = minimax_helper(result(board, action), X, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: break
        return min_eval