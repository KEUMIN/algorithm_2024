# 프로그래머스 - 여행경로 : https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 사용 알고리즘 : DFS

from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    used = defaultdict(bool)

    for ticket in tickets:
        f, t = ticket
        graph[f].append(t)
        used[f + t] = False

    for ls in graph.values():
        ls.sort()

    def dfs(start, route):
        if all(v for v in used.values()):
            return route[:]

        answer = []
        for end in graph[start]:
            if not used[start + end]:
                route.append(end)
                used[start + end] = True
                answer = dfs(end, route)

        return answer

    return dfs("ICN", ["ICN"])


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
