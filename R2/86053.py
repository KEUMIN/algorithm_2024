import math


def solution(a, b, g, s, w, t):
    def is_possible(time):
        total_gold, total_silver, total_all = 0, 0, 0
        for i in range(len(g)):
            trips = math.ceil((time // t[i]) / 2)

            total_gold += min(g[i], w[i] * trips)
            total_silver += min(s[i], w[i] * trips)
            total_all += min(g[i] + s[i], w[i] * trips)

        return total_gold >= a and total_silver >= b and total_all >= a + b

    left, right = 0, 10**15
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
