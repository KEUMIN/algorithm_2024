# 프로그래머스 - 징검다리 건너기 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 사용 알고리즘 : 이진 탐색
def solution(stones, k):
    def can_cross(mid):
        count = 0
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:
                    return False
            else:
                count = 0
        return True

    left, right = 1, max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
