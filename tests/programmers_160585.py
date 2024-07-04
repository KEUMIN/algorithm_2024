def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def solution(board):
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)
    
    if not (x_count == o_count or x_count + 1 == o_count):
        return 0
    
    o_wins = check_winner(board, 'O')
    x_wins = check_winner(board, 'X')
    
    if o_wins and x_wins:
        return 0
    
    if o_wins and o_count != x_count + 1:
        return 0
    
    if x_wins and o_count != x_count:
        return 0
    
    return 1
