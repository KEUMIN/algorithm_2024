# 프로그래머스 - 혼자서 하는 틱택토 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 사용 알고리즘 : 시뮬레이션


def solution(board):
    cnt_o = sum(board[i].count("O") for i in range(3))
    cnt_x = sum(board[i].count("X") for i in range(3))

    o_win = is_game_won_by("O", board)
    x_win = is_game_won_by("X", board)

    if o_win and x_win:
        return 0
    elif o_win and (cnt_o != cnt_x + 1):
        return 0
    elif x_win and (cnt_o != cnt_x):
        return 0
    elif not (cnt_o == cnt_x or cnt_o == cnt_x + 1):
        return 0
    else:
        return 1


def is_game_won_by(player, board):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(
            board[j][i] == player for j in range(3)
        ):
            return True
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False
