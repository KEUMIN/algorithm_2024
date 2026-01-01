from collections import deque


def solution(board):
    N = len(board)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    min_cost = [[[float('INF')] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque([(0, 0, -1, 0)])

    while queue:
        x, y, d, cost = queue.popleft()
        for i, (dx, dy) in enumerate(directions):
            mx, my = dx+ x, dy + y
            if 0 <= mx < N and 0 <= my < N and board[mx][my] == 0:
                cur_cost = cost + 100
                if d != -1 and d != i:
                    cur_cost += 500
                if min_cost[mx][my][i] > cur_cost:
                    min_cost[mx][my][i] = cur_cost
                    queue.append((mx, my, i, cur_cost))

    return min(min_cost[N - 1][N - 1])