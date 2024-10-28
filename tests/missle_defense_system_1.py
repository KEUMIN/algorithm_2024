# 프로그래머스 - 요격 시스템 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/181188
# 사용 알고리즘 : 그리디
# 인사이트 : 첫 풀이에서는 시작 포인트와 끝 포인트를 분리해서 작업했는데, 이는 잘못된 결과를 낳았음.


def solution(targets):
    result = 1
    targets.sort(key=lambda x: x[1])
    end_point = targets[0][1]

    for i in range(1, len(targets)):
        s, e = targets[i]
        if s >= end_point:
            result += 1
            end_point = e

    return result
