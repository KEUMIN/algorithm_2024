# 프로그래머스 - 메뉴 리뉴얼 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/72411
# 사용 알고리즘 : 완전 탐색 & 조합
from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    result = []

    def put_popular_menu(course_dict):
        max_order = max(course_dict.values())
        if max_order > 1:
            for k, v in course_dict.items():
                if v == max_order:
                    result.append(k)

    for num in course:
        course_dict = defaultdict(int)
        for order in orders:
            for combi in combinations(sorted(order), num):
                course_dict["".join(combi)] += 1
        if course_dict:
            put_popular_menu(course_dict)

    return sorted(result)
