# 프로그래머스 - 연속 펄스 부분 수열의 합 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/161988
# 사용 알고리즘 : DP
def solution(sequence):
    a = [num * 1 if i % 2 == 0 else num * -1 for i, num in enumerate(sequence)]
    b = [num * -1 if i % 2 == 0 else num * 1 for i, num in enumerate(sequence)]

    return max(max_subarray_sum(a), max_subarray_sum(b))


# Kadane's Algorithm
def max_subarray_sum(nums):
    # 초기값 설정
    max_sum = float("-inf")  # 가장 큰 합
    current_sum = 0  # 현재 부분합

    for num in nums:
        # 현재 값을 포함한 합과 현재 값 중 더 큰 값을 선택
        current_sum = max(num, current_sum + num)
        # 최대 합 갱신
        max_sum = max(max_sum, current_sum)

    return max_sum
