import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    gate_set = set(gates)
    summit_set = set(summits)

    # 무방향 그래프
    graph = defaultdict(list)
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    INF = 10**18
    intensity = [INF] * (n + 1)

    # 모든 출입구를 0으로 시작하는 '다중 출발' 다익스트라
    pq = []
    for g in gates:
        intensity[g] = 0
        heapq.heappush(pq, (0, g))  # (현재까지의 intensity, 정점)

    while pq:
        cur_int, u = heapq.heappop(pq)
        if cur_int > intensity[u]:
            continue
        # 봉우리에서 더 확장할 필요 없음
        if u in summit_set:
            continue
        for v, w in graph[u]:
            # 다른 출입구로는 진입 금지
            if v in gate_set:
                continue
            new_int = max(cur_int, w)
            if new_int < intensity[v]:
                intensity[v] = new_int
                heapq.heappush(pq, (new_int, v))

    return sorted(
        [[summit, intensity[summit]] for summit in summits], key=lambda x: (x[1], x[0])
    )[0]
