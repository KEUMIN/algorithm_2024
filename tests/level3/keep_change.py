# 프로그래머스 - 거스름돈 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/12907
# 사용 알고리즘 : 동적 프로그래밍
def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n] % 1000000007
