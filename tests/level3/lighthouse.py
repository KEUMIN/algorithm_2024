# 프로그래머스 - 등대 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/133500
# 사용 알고리즘 : 그래프...
def solution(n, lighthouse):
    # 그래프 구성 - 각 노드의 연결 개수 저장
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)  # 각 노드의 연결 개수

    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # 리프 노드(연결이 1개인 노드)부터 처리
    answer = 0
    visited = [False] * (n + 1)

    while True:
        # 리프 노드 찾기
        leaves = []
        for i in range(1, n + 1):
            if not visited[i] and degree[i] == 1:
                leaves.append(i)

        if not leaves:
            break

        # 리프 노드의 인접 노드를 켜기
        for leaf in leaves:
            visited[leaf] = True
            # 리프 노드와 연결된 노드 찾기
            for adj in graph[leaf]:
                if not visited[adj]:
                    visited[adj] = True
                    answer += 1
                    # 인접한 노드들의 degree 감소
                    for next_node in graph[adj]:
                        if not visited[next_node]:
                            degree[next_node] -= 1

    return answer
