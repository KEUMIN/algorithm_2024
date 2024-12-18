# 프로그래머스 - 금과 은 운반하기 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/86053
# 사용 알고리즘 : 이진탐색
# 인사이트 : 시간을 중심으로 생각해서 0부터 최대 시간 사이 이진탐색으로 최소 시간을 찾는 것이 포인트
#          그리고 배달 가능 여부 구하는 함수 도출 또한 핵심.


def solution(a, b, g, s, w, t):
    def can_move_in(mid):
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

    left, right = 0, int(1e15)
    answer = right

    while left <= right:
        mid = (right - left) // 2
        if can_move_in(mid):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
            answer = mid

    return answer
