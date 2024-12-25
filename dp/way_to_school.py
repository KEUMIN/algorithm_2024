# 프로그래머스 - 등굣길 : https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 사용 알고리즘 : DP
def solution(m, n, puddles):
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점

    # 물웅덩이 위치를 set으로 변환 (검색 효율성을 위해)
    puddles = set((y, x) for x, y in puddles)

    # 모든 위치에 대해
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # 시작점은 건너뛰기
                continue

            if (i, j) in puddles:  # 물웅덩이는 0으로
                dp[i][j] = 0
            else:
                # 위쪽과 왼쪽에서 오는 경로의 합
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]
