# 프로그래머스 - 경주로 건설 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/67259
# 사용 알고리즘 : BFS
from collections import deque


def solution(board):
    N = len(board)
    visit = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 100, 0, 0))
    visit[0][0] = True
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    answer = float("inf")

    while queue:
        x, y, cost, px, py = queue.popleft()
        if x == N - 1 and y == N - 1:
            answer = min(answer, cost)

        for dx, dy in d:
            mx, my = x + dx, y + dy
            if 0 <= mx < N and 0 <= my < N and board:
                if not visit[mx][my] and board[mx][my] != 1:
                    new_cost = cost
                    if x == 0 and y == 0:
                        new_cost += 100
                    else:
                        if dx == px and dy == py:
                            new_cost += 100
                        else:
                            new_cost += 600

                    queue.append((mx, my, new_cost, dx, dy))
                    visit[mx][my] = True

    return answer


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
