# 카데인 알고리즘
def solution(sequence):
    def max_subarray_sum(arr):
        max_sum = cur_sum = arr[0]
        for num in arr[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

    pulse1 = [num if i % 2 == 0 else -num for i, num in enumerate(sequence)]
    pulse2 = [-num if i % 2 == 0 else num for i, num in enumerate(sequence)]

    return max(max_subarray_sum(pulse1), max_subarray_sum(pulse2))
