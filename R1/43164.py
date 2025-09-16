from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for t in sorted(tickets, key=lambda x: x[1], reverse=True):
        graph[t[0]].append(t[1])

    route, stack = [], ["ICN"]
    while stack:
        start = stack[-1]
        if graph[start]:
            stack.append(graph[start].pop())
        else:
            route.append(stack.pop())

    return route[::-1]


print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
