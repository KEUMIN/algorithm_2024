# 프로그래머스 - 요격 시스템 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/181188
# 사용 알고리즘 : 그리디
# 인사이트 : 단속 카메라 (LV3)와 같은 문제, 끝점을 기준으로 정렬하여, 시작점이 넘는지 검증하면서 순회하는 방식


def solution(targets: list):
    targets.sort(key=lambda x: x[1])
    tmp_end = targets[0][1]
    result = 1

    for i in range(1, len(targets)):
        if targets[i][0] >= tmp_end:
            tmp_end = targets[i][1]
            result += 1

    return result
