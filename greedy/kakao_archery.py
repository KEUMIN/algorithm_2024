# 프로그래머스 - 양궁대회 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/92342
# 사용 알고리즘 : 그리디, 중복조합, 완전탐색
from itertools import combinations_with_replacement


def solution(n, info):
    max_info = []
    max_diff = 0

    def get_max_diff(ryan_info, cur_diff):
        nonlocal max_diff
        nonlocal max_info

        if cur_diff > max_diff:
            max_diff = cur_diff
            max_info = ryan_info
            print(cur_diff)
            print(ryan_info)

    def get_info_diff(ryan_info):
        diff = 0
        for i in range(len(info)):
            if ryan_info[i] > info[i]:
                diff += 10 - i
            elif info[i] > 0:
                diff -= 10 - i
        return diff

    def get_ryan_info(combi):
        ryan_info = [0] * len(info)
        for i in combi:
            ryan_info[10 - i] += 1
        return ryan_info

    for combi in combinations_with_replacement(range(11), n):
        ryan_info = get_ryan_info(combi)
        cur_diff = get_info_diff(ryan_info)
        get_max_diff(ryan_info, cur_diff)

    return max_info if max_diff > 0 else [-1]
