import random
from game.logic import check_winner

def minimax(board, player):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if "-" not in board: return 0

    if player == "O":
        best_score = -999
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, "X")
                board[i] = "-"
                best_score = max(best_score, score)
        return best_score

    else:
        best_score = 999
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, "O")
                board[i] = "-"
                best_score = min(best_score, score)
        return best_score


def get_ai_move(board, difficulty):
    # EASY → random move
    if difficulty == "easy":
        choices = [i for i in range(9) if board[i] == "-"]
        return random.choice(choices)

    # MEDIUM → 50% minimax, 50% random
    if difficulty == "medium":
        if random.random() < 0.5:
            choices = [i for i in range(9) if board[i] == "-"]
            return random.choice(choices)

    # HARD → unbeatable AI
    best_score = -999
    best_move = None

    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(board, "X")
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i

    return best_move
