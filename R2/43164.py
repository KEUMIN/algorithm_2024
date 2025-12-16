from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    for s, e in sorted(tickets, key=lambda x: x[1], reverse=True):
        graph[s].append(e)

    route = []

    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        route.append(node)

    dfs("ICN")
    return route[::-1]
