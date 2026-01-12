def solution(info, edges):
    answer = set()
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(current_sheep, current_wolf, next_nodes):
        answer.add(current_sheep)

        for next_node in next_nodes:
            sheep = current_sheep
            wolf = current_wolf

            if info[next_node] == 0:
                sheep += 1
            else:
                wolf += 1

            if wolf >= sheep:
                continue

            new_next_nodes = next_nodes - {next_node}
            new_next_nodes.update(graph[next_node])
            dfs(sheep, wolf, new_next_nodes)

    dfs(1, 0, set(graph[0]))

    return max(answer)
