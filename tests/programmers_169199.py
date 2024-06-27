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
    
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    def bfs():
        while q:
            x, y, d = q.popleft()
            for i in range(len(dx)):
                mx = x
                my = y
                while 0 <= mx and mx < rl and 0 <= my and my < cl and board[mx][my] != 'D':
                    mx += dx[i]
                    my += dy[i]
                    
                mx -= dx[i]
                my -= dy[i]
                
                if v[mx][my] == True:
                    continue
                elif board[mx][my] == 'G':
                    return d + 1
                
                q.append((mx, my, d+1))
                v[mx][my] = True
                
        return -1
    
    return bfs()


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))