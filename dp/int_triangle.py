#43105
#DP
def solution(triangle):
    n = len(triangle)
    sums = [[0] * n for _ in range(n)]
    sums[0][0] = triangle[0][0]
    for i in range(n - 1):
        for j in range(i + 1):
            sums[i + 1][j] = max(sums[i + 1][j], sums[i][j] + triangle[i + 1][j])
            sums[i + 1][j + 1] = max(sums[i + 1][j + 1], sums[i][j] + triangle[i + 1][j + 1])
    return max(sums[n - 1])

#DFS
def solution_dfs(triangle):
    def dfs(node):
        nonlocal max_val
        idx, dep, sum = node
        if dep == len(triangle) - 1:
            max_val = max(max_val, sum)
            return
        for i in range(2):
            dfs((idx + i, dep + 1, sum + triangle[dep + 1][idx + i]))
            
    max_val = 0
    dfs((0, 0, triangle[0][0]))
    return max_val

# print(solution_dfs([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))