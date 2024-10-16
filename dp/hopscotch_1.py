# 프로그래머스 - 땅따먹기 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 사용 알고리즘 : 동적 프로그래밍 [점화식]


def solution(land):
    ln = len(land)
    sum = [[0] * 4 for _ in range(ln)]
    sum[0] = land[0]
    for i in range(1, ln):
        for j in range(4):
            sum[i][j] = max(sum[i - 1][:j] + sum[i - 1][j + 1 :]) + land[i][j]

    return max(sum[ln - 1])
