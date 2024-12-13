# 프로그래머스 - 택배 배달과 수거하기 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 사용 알고리즘 : 그리디


def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0  # 배달해야 할 박스 수
    p = 0  # 수거해야 할 박스 수

    # 가장 먼 집부터 처리
    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        # 현재 위치에서 배달과 수거가 필요한 경우
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2  # 왕복 거리

    return answer


print(solution(2, 4, [1, 0, 3, 1], [0, 3, 0, 4]))
