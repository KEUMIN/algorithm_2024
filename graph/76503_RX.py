# 트리는 임의의 정점을 루트로 잡아도 트리이다.


def solution(a, edges):
    n = len(a)
    # 전체 합이 0이 아니면 절대 전부 0으로 만들 수 없음
    if sum(a) != 0:
        return -1

    # 인접 리스트
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    # 재귀 없이 스택으로 부모/순서 계산 (루트 0)
    parent = [-1] * n
    parent[0] = 0
    order = []
    stack = [0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)

    # 후위 순회로 아래에서 위로 가중치 이동
    ans = 0
    for u in reversed(order[1:]):  # 루트(0)는 제외
        p = parent[u]
        ans += abs(a[u])  # u -> p로 옮기는 데 드는 횟수
        a[p] += a[u]  # 실질적으로 가중치를 위로 이동
        a[u] = 0

    # 루트까지 모였을 때 sum(a)==0 이므로 루트도 0이 됨
    return ans
