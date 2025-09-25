def solution(n, costs):
    parents = [i for i in range(n)]
    rank = [0] * n

    num_of_paths = 0
    tot_costs = 0

    for a, b, cost in sorted(costs, key=lambda x: x[2]):
        if num_of_paths == n - 1:
            return tot_costs
        if find(a, parents) != find(b, parents):
            union(a, b, parents, rank)
            num_of_paths += 1
            tot_costs += cost

    return tot_costs


def find(x, parents):
    if x == parents[x]:
        return parents[x]
    return find(parents[x], parents)


def union(x, y, parents, rank):
    root_x = find(x, parents)
    root_y = find(y, parents)

    if rank[root_x] > rank[root_y]:
        parents[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x
        rank[root_x] += 1
