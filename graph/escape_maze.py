#159993
from collections import deque

def solution(maps):
    def find_position(target):
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == target:
                    return i, j
        return None

    def bfs(start, end):
        queue = deque([(start[0], start[1], 0)])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[start[0]][start[1]] = True

        while queue:
            x, y, distance = queue.popleft()

            if (x, y) == end:
                return distance

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))

        return -1

    start = find_position('S')
    lever = find_position('L')
    exit = find_position('E')

    to_lever = bfs(start, lever)
    if to_lever == -1:
        return -1

    to_exit = bfs(lever, exit)
    if to_exit == -1:
        return -1

    return to_lever + to_exit