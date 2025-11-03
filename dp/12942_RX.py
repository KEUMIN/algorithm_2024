def solution(matrix_sizes):
    """
    matrix_sizes: [[r1,c1],[r2,c2],...,[rn,cn]]
    반환값: 모든 행렬을 곱할 때 필요한 최소 곱셈 연산 수 (정수)
    """
    n = len(matrix_sizes)
    # 차원 배열 p 만들기: A_i의 크기는 p[i-1] x p[i]
    # 예) [[5,3],[3,10],[10,6]] -> p = [5,3,10,6]
    p = [matrix_sizes[0][0]] + [c for _, c in matrix_sizes]

    # dp[i][j]: i번째~j번째 행렬을 모두 곱하는 최소 곱셈 수 (1-indexed로 생각)
    INF = 10**18
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 구간 길이 len=2..n 에 대해 증가시키며 채운다
    for length in range(2, n + 1):  # 부분 체인의 길이
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = INF
            # 마지막 분할 위치 k를 모두 시도
            for k in range(i, j):
                # (i..k) 먼저 곱하고, (k+1..j) 먼저 곱한 뒤, 두 결과를 곱하는 비용
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


print(solution([[5, 3], [3, 10], [10, 6]]))
