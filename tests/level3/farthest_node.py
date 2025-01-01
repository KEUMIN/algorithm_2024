# 프로그래머스 - 가장 먼 노드 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 사용 알고리즘 : BFS
from collections import defaultdict, deque


def solution(n, vertex):
    adj = defaultdict(list)
    for a, b in vertex:
        adj[a].append(b)
        adj[b].append(a)

    visit = [False] * (n + 1)
    distance = [0] * (n + 1)
    queue = deque([1])
    visit[1] = True

    while queue:
        cur_node = queue.popleft()
        for neighbor in adj[cur_node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                distance[neighbor] = distance[cur_node] + 1
                queue.append(neighbor)

    max_distance = max(distance)
    return distance.count(max_distance)
