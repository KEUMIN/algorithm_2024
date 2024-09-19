# 42861 - 유니온 파인드, 최소 신장 트리

def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    elif rank[yroot] > rank[xroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    sum_of_path = 0
    num_of_edges = 0

    for cost in costs:
        if num_of_edges == n - 1:
            break
        x, y, price = cost
        if find(parent, x) != find(parent, y):
            union(parent, rank, x, y)
            sum_of_path += price
            num_of_edges += 1

    return sum_of_path