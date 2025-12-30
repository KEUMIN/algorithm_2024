from collections import deque


def solution(board):
    N = len(board)
    min_cost = [[[float("INF")] * 4 for _ in range(N)] for _ in range(N)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([])

    queue.append((0, 0, 0, -1))

    for i in range(4):
        min_cost[0][0][i] = 0

    while queue:
        cx, cy, cost, prev_dir = queue.popleft()

        for i, (dx, dy) in enumerate(directions):
            mx, my = cx + dx, cy + dy

            if 0 <= mx < N and 0 <= my < N and board[mx][my] == 0:
                new_cost = cost + 100
                if prev_dir != -1 and prev_dir != i:
                    new_cost += 500

                if new_cost < min_cost[mx][my][i]:
                    min_cost[mx][my][i] = new_cost
                    queue.append((mx, my, new_cost, i))

    return min(min_cost[N - 1][N - 1])
