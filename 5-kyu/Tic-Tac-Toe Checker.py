# kata: https://www.codewars.com/kata/525caa5c1bf619d28c000335
def is_solved(board):
    reversed_board = [[board[x][y] for x in range(3)] for y in range(3)]
    is_empty = False

    if board[0][0] == board[1][1] == board[2][2] == 1:
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == 2:
        return 2
    elif board[0][2] == board[1][1] == board[2][0] == 1:
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == 2:
        return 2

    for row in board:
        if all(map( lambda cell: cell == 1, row)):
            return 1
        elif all(map( lambda cell: cell == 2, row)):
            return 2
        elif any(map( lambda cell: cell == 0, row)):
            is_empty = True

    for column in reversed_board:
        if all(map( lambda cell: cell == 1, column)):
            return 1
        elif all(map( lambda cell: cell == 2, column)):
            return 2
        elif any(map( lambda cell: cell == 0, column)):
            is_empty = True

    if is_empty:
        return -1
    else:
        return 0