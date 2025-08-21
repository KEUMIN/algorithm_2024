def solution(stones, k):
    def can_cross(mid):
        # mid 값으로 건널 수 있는지 확인하는 함수
        count = 0
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:  # k개의 연속된 돌을 건너뛸 수 없으면 실패
                    return False
            else:
                count = 0
        return True

    # 이진 탐색 초기화
    left, right = 1, max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            answer = mid  # 가능한 경우, 정답을 갱신하고 더 큰 값을 탐색
            left = mid + 1
        else:
            right = mid - 1  # 불가능한 경우, 더 작은 값을 탐색

    return answer
