# def solution(m, n, puddles):
#     g = [[(0, False)] * m for _ in range(n)]
#     for px, py in puddles:
#         g[py - 1][px - 1] = (0, True)
#
#     for i in range(m):
#         for j in range(n):
#             if i == 0 and j == 0:
#                 g[j][i] = (1, False)
#                 continue
#
#             if g[j][i][1]:
#                 continue
#             left_cnt = g[j - 1][i][0] if j - 1 >= 0 and not g[j - 1][i][1] else 0
#             upper_cnt = g[j][i - 1][0] if i - 1 >= 0 and not g[j][i - 1][1] else 0
#             g[j][i] = ((left_cnt + upper_cnt) % 1_000_000_007, False)
#
#     return g[n - 1][m - 1][0]


# 한 행으로 공간복잡도를 줄이고 각 값마다 나머지를 할당함으로써 연산 속도를 올리는 풀이.
def solution(m, n, puddles):
    MOD = 1_000_000_007
    water = {tuple(p) for p in puddles}  # (x, y)
    dp = [0] * m
    dp[0] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in water:
                dp[x - 1] = 0
            elif x > 1:
                dp[x - 1] = (dp[x - 1] + dp[x - 2]) % MOD
    return dp[-1]
