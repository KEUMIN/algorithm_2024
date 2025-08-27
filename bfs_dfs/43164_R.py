from collections import defaultdict


# 스택 DFS
def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets, key=lambda x: x[1], reverse=True):
        graph[a].append(b)

    route, stack = [], ["ICN"]
    while stack:
        cur = stack[-1]
        if graph[cur]:  # 더 갈 곳이 있으면 스택에 push
            stack.append(graph[cur].pop())
        else:  # 막다른 길이면 경로에 기록하며 backtrack
            route.append(stack.pop())

    return route[::-1]


# 백트래킹 DFS
def solution2(tickets):
    tickets.sort()  # 사전순 우선 탐색을 위해 정렬
    used = [False] * len(tickets)
    path = ["ICN"]

    def dfs(cur, depth):
        if depth == len(tickets):  # 모든 티켓 사용 완료
            return True
        for i, (a, b) in enumerate(tickets):
            if not used[i] and a == cur:
                used[i] = True
                path.append(b)
                if dfs(b, depth + 1):  # 처음 완성되는 경로가 사전순 최소
                    return True
                path.pop()
                used[i] = False
        return False

    dfs("ICN", 0)
    return path


solution(
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
)
