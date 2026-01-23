import math


def solution(a, b, g, s, w, t):
    def is_possible(time):
        tot_silver, tot_gold, tot_all = 0, 0, 0
        for i in range(len(g)):
            trips = math.ceil((time // t[i]) / 2)
            max_weight = trips * w[i]

            tot_gold += min(g[i], max_weight)
            tot_silver += min(s[i], max_weight)
            tot_all += min(s[i] + g[i], max_weight)

        return tot_gold >= a and tot_silver >= b and tot_all >= a + b

    left, right = 1, 10**15
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
