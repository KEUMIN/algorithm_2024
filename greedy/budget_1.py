# 프로그래머스 - 예산 (LV1) : https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 접근 : 1. 오름차순으로 정렬한다
#       2. 총 예산에서 순회하며 삭감한다


def solution(d, budget):
    sorted_d = sorted(d)
    max_cnt = 0
    for dept in sorted_d:
        if budget >= dept:
            budget -= dept
            max_cnt += 1
        else:
            break
    return max_cnt
