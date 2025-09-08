def solution(a):
    n = len(a)
    right_min = [0] * n
    m = float("inf")
    for i in range(n - 1, -1, -1):
        m = a[i] if a[i] < m else m
        right_min[i] = m

    ans, left = 0, float("inf")
    for i, x in enumerate(a):
        left = x if x < left else left
        if x <= left or x <= right_min[i]:
            ans += 1
    return ans
