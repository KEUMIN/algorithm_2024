def solution(n):
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 1000000007)
    return fib[n]