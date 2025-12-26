def solution(stones, k):
    def can_pass(num):
        cnt = 0

        for stone in stones:
            if stone - num < 0:
                cnt += 1
                if cnt == k:
                    return False
            else:
                cnt = 0
        return True

    start = 0
    end = 200_000_000
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        if can_pass(mid):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
