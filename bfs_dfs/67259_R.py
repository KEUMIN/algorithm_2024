from collections import deque


def solution(board):
    N = len(board)
    # 비용을 저장할 3D 배열: cost[x][y][dir] -> (x, y) 위치에 dir 방향으로 도달하는 최소 비용
    cost = [[[float("inf")] * 4 for _ in range(N)] for _ in range(N)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    # BFS를 위한 큐
    queue = deque()
    for i in range(4):  # 초기 시작점에서 모든 방향으로 출발
        cost[0][0][i] = 0
        queue.append((0, 0, i, 0))  # x, y, dir, current_cost

    while queue:
        x, y, dir, current_cost = queue.popleft()

        # 목적지에 도달했으면 continue
        if x == N - 1 and y == N - 1:
            continue

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                # 새로운 비용 계산
                new_cost = current_cost + (
                    100 if dir == i else 600
                )  # 같은 방향: 100, 코너: 600

                # 최소 비용 갱신이 가능하면 큐에 추가
                if cost[nx][ny][i] > new_cost:
                    cost[nx][ny][i] = new_cost
                    queue.append((nx, ny, i, new_cost))

    # (N-1, N-1) 위치에서 모든 방향에 대해 최소 비용 반환
    return min(cost[N - 1][N - 1])
