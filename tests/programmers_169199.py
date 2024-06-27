from collections import deque

def solution(board):
    rl = len(board)
    cl = len(board[0])
    
    v = [[False]*cl for _ in range(rl)]
    q = deque()
    
    for i in range(rl):
        for j in range(cl):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                v[i][j] = True
    
    dr = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
    def bfs():
        while q:
            x, y, d = q.popleft()
            for dx, dy in dr:
                mx = x
                my = y
                while 0 <= mx + dx < rl and 0 <= my + dy < cl and board[mx + dx][my + dy] != 'D':
                    mx += dx
                    my += dy
                
                if v[mx][my]:
                    continue
                elif board[mx][my] == 'G':
                    return d + 1
                
                q.append((mx, my, d+1))
                v[mx][my] = True
                
        return -1
    
    return bfs()


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))