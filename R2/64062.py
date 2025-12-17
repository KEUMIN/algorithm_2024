def solution(stones, k):
    def can_pass(n):
        cnt = 0
        for s in stones:
            if s - n < 0:
                cnt += 1
                if cnt == k:
                    return False
            else:
                cnt = 0
        return True

    left = 1
    right = max(stones)
    answer = 1

    while left <= right:
        mid = (left + right) // 2
        if can_pass(mid):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer