# 프로그래머스 - 단속 카메라 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 사용 알고리즘 : 그리디
# 인사이트 : 요격 시스템 (LV2)와 동일한 문제


def solution(routes):
    routes.sort(key=lambda x: x[1])

    prev_exit = routes[0][1]
    result = 1
    for i in range(1, len(routes)):
        if prev_exit < routes[i][0]:
            prev_exit = routes[i][1]
            result += 1

    return result
