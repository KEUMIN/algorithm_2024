def solution(n, money):
    m = [0] * (n + 1)
    m[0] = 1

    for coin in money:
        for i in range(coin, n + 1):
            m[i] = (m[i - coin] + m[i]) % 1_000_000_007

    return m[n]