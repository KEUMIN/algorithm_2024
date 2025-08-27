from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    rm = defaultdict(list)
    ss = set()
    for r in roads:
        rm[r[0]].append(r[1])
        rm[r[1]].append(r[0])

    for s in sources:
        ss.add(s)

    c = [-1] * (n + 1)
    visit = [False] * (n + 1)

    q = deque([(destination, 0)])
    visit[destination] = True

    while q:
        cur_n, cur_c = q.popleft()

        if cur_n in ss:
            c[cur_n] = cur_c

        for n in rm[cur_n]:
            if not visit[n]:
                q.append((n, cur_c + 1))
                visit[n] = True

    return [c[s] for s in sources]


# visit과 destination이 필요 없는 풀이...
def solution2(n, roads, sources, destination):
    # 인접 리스트
    g = [[] for _ in range(n + 1)]
    for a, b in roads:
        g[a].append(b)
        g[b].append(a)

    # destination에서 시작하는 BFS (역으로 한 번만)
    dist = [-1] * (n + 1)
    dq = deque([destination])
    dist[destination] = 0

    while dq:
        cur = dq.popleft()
        for nxt in g[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                dq.append(nxt)

    # 요청된 source 순서대로 결과 반환
    return [dist[s] for s in sources]
