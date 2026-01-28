from collections import defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    for f, t in edges:
        graph[f].append(t)

    answer = 0

    def dfs(sheep, wolves, nodes):
        nonlocal answer
        answer = max(answer, sheep)

        for n in nodes:
            cur_sheep = sheep
            cur_wolves = wolves

            if info[n]:
                cur_wolves += 1
            else:
                cur_sheep += 1

            if cur_wolves >= cur_sheep:
                continue

            new_nodes = nodes - {n}
            new_nodes.update(graph[n])

            dfs(cur_sheep, cur_wolves, new_nodes)

    dfs(0, 0, {0})

    return answer
