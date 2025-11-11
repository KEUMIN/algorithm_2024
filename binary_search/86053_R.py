def solution(a, b, g, s, w, t):

    def can_deliver_in_time(mid):
        total_gold, total_silver, total = 0, 0, 0

        for i in range(len(g)):
            trips = mid // (2 * t[i])  # 왕복 횟수
            if mid % (2 * t[i]) >= t[i]:  # 편도 가능 여부
                trips += 1
            max_transport = trips * w[i]

            gold = min(g[i], max_transport)
            silver = min(s[i], max_transport)
            mixed = min(g[i] + s[i], max_transport)

            total_gold += gold
            total_silver += silver
            total += mixed

        return total_gold >= a and total_silver >= b and total >= a + b

    left, right = 0, int(1e15)  # 충분히 큰 값을 설정
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_deliver_in_time(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
