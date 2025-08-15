def solution(n, stations, w):
    coverage = 2 * w + 1
    result = 0
    start = 1

    for s in stations + [n + w + 1]:
        gap = (s - w) - start
        if gap > 0:
            result += (gap + coverage - 1) // coverage
        start = s + w + 1

    return result