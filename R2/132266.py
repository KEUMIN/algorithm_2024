from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    source_set = set(sources)
    shorts = [-1] * (n + 1)
    visit = [False] * (n + 1)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([(destination, 0)])
    visit[destination] = True

    while q:
        cur_node, cost = q.popleft()

        if cur_node in source_set:
            shorts[cur_node] = cost

        for n in graph[cur_node]:
            if not visit[n]:
                q.append((n, cost + 1))
                visit[n] = True

    return [shorts[i] for i in sources]
