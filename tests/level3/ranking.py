# 프로그래머스 - 순위 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 사용 알고리즘 : 플로이드-워셜 (어려움: *****)
def solution(n, results):
    # 승패 그래프 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 경기 결과 반영
    for winner, loser in results:
        graph[winner][loser] = True

    # 플로이드-워셜 알고리즘으로 모든 쌍의 승패 관계 갱신
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    # 순위를 확정할 수 있는 선수 수 계산
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:  # i가 j를 이기거나 j가 i를 이기는 경우
                count += 1
        if count == n - 1:  # 다른 모든 선수들과의 승패 관계가 확정된 경우
            answer += 1

    return answer
