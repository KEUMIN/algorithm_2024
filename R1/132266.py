from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    costs = [-1] * (n + 1)
    graph = defaultdict(list)
    source_set = set(sources)
    for p1, p2  in roads:
        graph[p1].append(p2)
        graph[p2].append(p1)

    queue = deque([(destination, 0)])
    visit = [False] * (n + 1)
    visit[destination] = True

    while queue:
        cur_n, cost = queue.popleft()

        if cur_n in source_set:
            costs[cur_n] = cost

        for neighbor in graph[cur_n]:
            if not visit[neighbor]:
                queue.append((neighbor, cost + 1))
                visit[neighbor] = True

    return [costs[s] for s in sources]