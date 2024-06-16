def unique_path(m, n):
    visit = [[-1]*n for _ in range(m)]

    def dp(x, y):
        if x == 0 or y == 0:
            return 1
        
        if visit[x][y] == -1:
            visit[x][y] = dp(x - 1, y) + dp(x, y - 1)

        return visit[x][y]
    
    return dp(m - 1, n - 1)

print(unique_path(3, 2))