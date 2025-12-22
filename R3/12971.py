def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)

    arr1 = sticker[:-1]
    arr2 = sticker[1:]

    return max(get_max(arr1), get_max(arr2))


def get_max(arr):
    sum_arr = [0] * len(arr)
    sum_arr[0] = arr[0]
    sum_arr[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        sum_arr[i] = max(sum_arr[i - 1], (arr[i] + sum_arr[i - 2]))

    return max(sum_arr)
