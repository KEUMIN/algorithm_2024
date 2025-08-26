# 유니온-파인드는 집합 연산의 한 종류이다. 단순 최소 비용 구하는 게 아니라. parents의 루트는 해당 집합의 대표 라벨이라고 생각하는 편이 좋음.


def solution(n, costs):
    parents = [i for i in range(n)]
    rank = [0] * n

    num_of_pathes = 0
    tot_costs = 0
    for cost in sorted(costs, key=lambda x: x[2]):
        if num_of_pathes == n - 1:
            return tot_costs
        x, y, c = cost
        if find(x, parents) != find(y, parents):
            union(x, y, parents, rank)
            num_of_pathes += 1
            tot_costs += c
    return tot_costs


def find(x, parents):
    if parents[x] == x:
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
