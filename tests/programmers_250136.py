from collections import deque

def solution(land):
    row = len(land)
    col = len(land[0])
    result = [0] * col
    
    visit = [[False]*col for _ in range(row)]
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    q = deque()
    
    def bfs():
        visit_col = set()
        cnt = 0
        while q:
            x, y = q.popleft()
            visit_col.add(y)
            cnt += 1
            
            for d in directions:
                dx, dy = d
                if 0 <= x + dx < row and 0 <= y + dy < col:
                    if land[x+ dx][y + dy] == 1 and not visit[x + dx][y + dy]:
                        q.append((x + dx, y + dy))
                        visit[x + dx][y + dy] = True
                        
        for i in visit_col:
            result[i] += cnt
            
                        
    for j in range(col):
        for i in range(row):
            if land[i][j] != 0 and not visit[i][j]:
                q.append((i, j))
                visit[i][j] = True
                bfs()
                
    return max(result)
