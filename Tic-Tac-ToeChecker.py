def parse_board(board):
    rows = ["".join([str(board[i][j]) for j in range(3)]) for i in range(3)]
    cols = ["".join([str(board[i][j]) for i in range(3)]) for j in range(3)]
    diag = ["".join([str(board[i][i]) for i in range(3)])]
    anti_diag = ["".join([str(board[i][2 - i]) for i in range(3)])]
    return rows + cols + diag + anti_diag

def is_winner(triple):
    if triple == "111":
        return 1
    elif triple == "222":
        return 2
    else:
        return 0

def is_solved(board):
    if any(is_winner(triple) == 1 for triple in parse_board(board)):
        return 1
    elif any(is_winner(triple) == 2 for triple in parse_board(board)):
        return 2
    elif all(triple.find("0") == -1 for triple in parse_board(board)):
        return 0
    else:
        return -1

test_board = [[0, 0, 1],[0, 1, 2],[2, 1, 0]]

print(is_solved(test_board))