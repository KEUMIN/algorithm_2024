from collections import deque

def count_islands(grid):
    num_of_islands = 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]

    def bfs(x,y):
        move_x = [-1, 1, 0, 0]
        move_y = [0, 0, -1, 1]
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        
        while queue:
            cur_x, cur_y = queue.popleft()
            
            for i in range(len(move_x)):
                next_x = cur_x + move_x[i]
                next_y = cur_y + move_y[i]
                
                if 0 <= next_x and next_x < row and 0 <= next_y and next_y < col:
                    if not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
                    
                    
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and grid[i][j] == "1":
                bfs(i, j)
                num_of_islands += 1

    return num_of_islands
    

print(count_islands(grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['1', '1', '0', '1', '1']
]))