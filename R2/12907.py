def solution(n, money):
    arr = [0] * (n + 1)
    arr[0] = 1

    for m in money:
        for i in range(m, n + 1):
            arr[i] = (arr[i] + arr[i - m]) % 1_000_000_007

    return arr[n]
