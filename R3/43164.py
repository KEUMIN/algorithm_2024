from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for f, t in tickets:
        graph[f].append(t)

    for v in graph.values():
        v.sort(reverse=True)

    route = []

    def dfs(start_place):
        while graph[start_place]:
            destination = graph[start_place].pop()
            dfs(destination)
        route.append(start_place)

    dfs("ICN")

    return route[::-1]
