def solution(stones, k):
    def can_cross(mid):
        count = 0
        for s in stones:
            if s < mid:
                count += 1
                if count == k:
                    return False
            else:
                count = 0
        return True

    left, right = 1, max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer
