# 프로그래머스 - 리코쳇 로봇 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 사용 알고리즘 : BFS
from collections import deque


def solution(board):
    start_point = "R"
    finish_point = "G"
    obstacle = "D"

    row = len(board)
    col = len(board[0])
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    visit = [[False] * col for _ in range(row)]

    def find_point(point):
        nonlocal row, col
        for i in range(row):
            for j in range(col):
                if board[i][j] == point:
                    return (i, j)
        return (-1, -1)

    def can_move_to(x, y):
        nonlocal row, col, obstacle
        return (0 <= x < row and 0 <= y < col) and board[x][y] != obstacle

    def bfs(node):
        nonlocal finish_point
        x, y = node
        visit[x][y] = True
        queue = deque([(x, y, 0)])

        while queue:
            cx, cy, cnt = queue.popleft()
            if board[cx][cy] == finish_point:
                return cnt

            for dx, dy in d:
                tx, ty = cx, cy
                while can_move_to(tx + dx, ty + dy):
                    tx += dx
                    ty += dy
                if visit[tx][ty]:
                    continue
                else:
                    visit[tx][ty] = True
                    queue.append((tx, ty, cnt + 1))
        return -1

    return bfs(find_point(start_point))
