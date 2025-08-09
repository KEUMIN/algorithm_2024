import heapq


def solution(n, works):
    h = []
    for w in works:
        heapq.heappush(h, w * -1)

    while n > 0:
        tmp = heapq.heappop(h)
        if tmp == 0 : break
        heapq.heappush(h, tmp + 1)
        n -= 1

    return sum(e * e for e in h)

print(solution(4, [4, 3, 3]))