#12913
def solution(land):
    n = len(land)
    sum = [[0] * 4 for _ in range(n)]
    sum[0] = land[0]
    for i in range(1, n):
        for j in range(4):
            sum[i][j] = max(sum[i - 1][:j] + sum[i - 1][j + 1:]) + land[i][j]
    return max(sum[n -1])