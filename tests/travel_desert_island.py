from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    d = [(1,0),(0,-1),(-1,0),(0,1)]
    visit = [[False]*col for _ in range(row)]
    q = deque()
    
    def isValid(i, j, r, c):
        if 0 <= i < r and 0 <= j < c:
            if not visit[i][j] and maps[i][j] != 'X':
                return True
            else:
                return False
        else:
            return False
    
    def bfs(i, j, r, c):
        q.append((i, j))
        visit[i][j] = True
        sum = int(maps[i][j])
        
        while q:
            cx, cy = q.popleft()
            for dx, dy in d:
                if isValid(cx+dx, cy+dy, r, c):
                    visit[cx+dx][cy+dy] = True
                    q.append((cx+dx, cy+dy))
                    sum += int(maps[cx+dx][cy+dy])
                    
        return sum
    
    answer = []
    for i in range(row):
        for j in range(col):
            if isValid(i, j, row, col):
                answer.append(bfs(i, j, row, col))
                
    answer.sort()
                
    return answer if len(answer) > 0 else [-1]
        
        
maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))
