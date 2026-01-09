def solution(sequence):
    def get_max_part_sum(seq):
        sum_arr = [0] * len(seq)
        max_arr = [0] * len(seq)
        sum_arr[0] = seq[0]
        max_arr[0] = seq[0]

        for i in range(1, len(seq)):
            sum_arr[i] = max(sum_arr[i - 1] + seq[i], seq[i])
            max_arr[i] = max(max_arr[i - 1], sum_arr[i])

        return max(max_arr)

    return max(
        get_max_part_sum([n if i % 2 == 0 else -1 * n for i, n in enumerate(sequence)]),
        get_max_part_sum([-1 * n if i % 2 == 0 else n for i, n in enumerate(sequence)]),
    )
