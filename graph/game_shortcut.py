#1844
from collections import defaultdict, deque

def solution(map):
    row = len(map)
    col = len(map[0])
    direction_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    def bfs(start):
        visited = [[False] * col for _ in range(row)]
        sx, sy = start
        visited[sx][sy] = True
        queue = deque([(sx, sy, 1)])
        result = float('inf')
        
        while queue:
            cx, cy, cnt = queue.popleft()
            if cx == row - 1 and cy == col - 1:
                result = min(result, cnt)
            for dx, dy in direction_list:
                mx = cx + dx
                my = cy + dy
                if 0 <= mx < row and 0 <= my < col:
                    if not visited[mx][my] and map[mx][my] == 1:
                        visited[mx][my] = True
                        queue.append((mx, my, cnt + 1))
        return result if result != float('inf') else -1
    
    return bfs((0, 0))