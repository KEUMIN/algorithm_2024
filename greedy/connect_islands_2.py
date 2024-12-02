# 프로그래머스 - 섬 연결하기 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 사용 알고리즘 : 그리디, 유니온 파인드, 최소 신장 트리(Minimum Spanning Tree)
# 문제 핵심 키워드: "최소 비용", "모든 OO 연결" (다익스트라의 경우 특정 두 지점 연결 최소)
# 문제 풀이 핵심: 비용을 오름차순으로 먼저 정렬 후 순회한다.


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
    parents[x] = find(parents[x], parents)
    return parents[x]


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
