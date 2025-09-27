def solution(sequence):
    s1 = [s if i % 2 == 0 else -1 * s for i, s in enumerate(sequence)]
    s2 = [s if i % 2 != 0 else -1 * s for i, s in enumerate(sequence)]

    def get_max_sum(arr):
        N = len(arr)
        cur_sum, max_sum = [0] * N, [0] * N
        cur_sum[0], max_sum[0] = arr[0], arr[0]

        for i in range(1, N):
            cur_sum[i] = arr[i] if cur_sum[i - 1] + arr[i] < arr[i] else cur_sum[i - 1] + arr[i]
            max_sum[i] = max(max_sum[i - 1], cur_sum[i])

        return max(max_sum)

    return max(get_max_sum(s1), get_max_sum(s2))