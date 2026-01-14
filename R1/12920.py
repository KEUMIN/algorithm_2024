def solution(n, cores):
    # Phase 1.
    m = len(cores)

    def processed(time):
        return m + sum(time // c for c in cores)

    left, right = 1, max(cores) * n

    while left <= right:
        mid = (left + right) // 2
        if processed(mid) >= n:
            right = mid - 1
        else:
            left = mid + 1

    # Phase 2.
    t = left
    tasks = processed(t - 1)
    remain = n - tasks

    for i, c in enumerate(cores):
        if t % c == 0:
            remain -= 1
            if remain == 0:
                return i + 1
