def solution(n, cores):
    m = len(cores)

    def processed(time):
        return m + sum([time // c for c in cores])

    left, right = 1, n * max(cores)
    while left <= right:
        mid = (left + right) // 2
        if processed(mid) >= n:
            right = mid - 1
        else:
            left = mid + 1

    remain = n - processed(left - 1)
    for i, c in enumerate(cores):
        if left % c == 0:
            remain -= 1
            if remain == 0:
                return 1 + i