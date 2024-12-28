# 프로그래머스 - 여행경로 : https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 사용 알고리즘 : DFS

from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    # 그래프 생성 및 정렬
    for f, t in tickets:
        graph[f].append(t)
    for key in graph:
        graph[key].sort(reverse=True)  # 역순 정렬하여 pop()으로 처리

    route = []  # 최종 경로를 저장할 리스트

    def dfs(start):
        # 현재 공항에서 갈 수 있는 경로를 모두 탐색
        while graph[start]:
            next_dest = graph[start].pop()  # 정렬된 상태에서 pop()
            dfs(next_dest)
        route.append(start)  # 경로 추가

    dfs("ICN")
    return route[::-1]  # 경로를 뒤집어서 반환
