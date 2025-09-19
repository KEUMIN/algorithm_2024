from collections import deque


def solution(board):
    N = len(board)

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cost = [[[float('INF')] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque([])
    for i in range(4):
        cost[0][0][i] = 0
        queue.append((0,0,0,i))

    while queue:
        cx, cy, cur_cost, dir = queue.popleft()

        if cx == N - 1 and cy == N - 1:
            continue

        for i, (dx, dy) in enumerate(d):
            mx, my = cx + dx, cy + dy
            if 0 <= mx < N and 0 <= my < N and board[mx][my] == 0:
                new_cost = cur_cost + (100 if dir == i else 600)
                if cost[mx][my][i] > new_cost:
                    cost[mx][my][i] = new_cost
                    queue.append((mx, my, new_cost, i))

    return min(cost[N-1][N-1])

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))