from collections import defaultdict


def solution(info, edges):
    answer = 1
    graph = defaultdict(list)
    for f, t in edges:
        graph[f].append(t)

    def dfs(sheep, wolves, next_nodes):
        nonlocal answer
        answer = max(sheep, answer)

        for n in next_nodes:
            cur_sheep = sheep
            cur_wolves = wolves

            if info[n]:
                cur_wolves += 1
            else:
                cur_sheep += 1

            if cur_wolves >= cur_sheep:
                continue

            new_next_nodes = next_nodes - {n}
            new_next_nodes.update(graph[n])
            dfs(cur_sheep, cur_wolves, new_next_nodes)

    dfs(1, 0, set(graph[0]))
    return answer
