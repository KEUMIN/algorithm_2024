from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    sources_set = set(sources)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    visit = [False] * (n + 1)
    costs = [-1] * (n + 1)

    q = deque([(destination, 0)])
    visit[destination] = True

    while q:
        cur_node, cost = q.popleft()

        if cur_node in sources_set:
            costs[cur_node] = cost

        for neighbor in graph[cur_node]:
            if not visit[neighbor]:
                q.append((neighbor, cost + 1))
                visit[neighbor] = True

    return [costs[i] for i in sources]
