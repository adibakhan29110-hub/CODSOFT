def check_winner(board):
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win:
        if board[a] == board[b] == board[c] != "-":
            return board[a]
    return None

def is_draw(board):
    return "-" not in board and check_winner(board) is None
