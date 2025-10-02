def solution(n, costs):
    parent = [i for i in range(n)]
    rank = [0] * n
    num_of_path = 0
    tot_cost = 0

    for x, y, c in sorted(costs, key= lambda x: x[2]):
        if num_of_path == n - 1:
            return tot_cost

        if find(x, parent) != find(y, parent):
            union(x, y, parent, rank)
            num_of_path += 1
            tot_cost += c

    return tot_cost



def find(x, parent):
    if parent[x] == x:
        return parent[x]
    return find(parent[x], parent)


def union(x, y, parent, rank):
    parent_x, parent_y = find(x, parent), find(y, parent)

    if rank[parent_x] > rank[parent_y]:
        parent[parent_y] = parent_x
    elif rank[parent_y] > rank[parent_x]:
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x
        rank[parent_x] += 1


solution(4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
