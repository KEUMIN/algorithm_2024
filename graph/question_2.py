from collections import deque

def short_path(grid):
    result = -1
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while queue:
        cur_x, cur_y, cur_dimension = queue.popleft()
        if cur_x == row - 1 and cur_y == col - 1:
            result = cur_dimension
            break
        
        m_x = [1, 1, 0, -1, 1, -1, 0, -1]
        m_y = [1, 0, 1, 1, -1, 0, -1, -1]
        
        for i in range(len(m_x)):
            moved_x = cur_x + m_x[i]
            moved_y = cur_y + m_y[i]

            if 0 <= moved_x and moved_x < row and 0 <= moved_y and moved_y < col:
                if grid[moved_x][moved_y] == 0 and not visited[moved_x][moved_y]:
                    visited[moved_x][moved_y] = True
                    queue.append((moved_x, moved_y, cur_dimension + 1))

    return result
    

print(short_path(grid = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 0]
]))