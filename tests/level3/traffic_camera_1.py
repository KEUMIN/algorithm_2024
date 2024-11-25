# 프로그래머스 - 단속 카메라 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 사용 알고리즘 : 그리디
# 인사이트 : 요격 시스템 (LV2)와 동일한 문제, 경계값에 대한 이해 필요


def solution(routes):
    result = 1
    routes.sort(key=lambda x: x[1])
    cur_end = routes[0][1]

    for i in range(1, len(routes)):
        if routes[i][0] > cur_end:
            cur_end = routes[i][1]
            result += 1

    return result
