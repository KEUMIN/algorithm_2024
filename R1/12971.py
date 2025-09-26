def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker)

    N = len(sticker)
    arr1 = [0] * N
    arr2 = [0] * N

    dp(0, N - 1, arr1, sticker)
    dp(1, N, arr2, sticker)

    return max(arr1[N - 2], arr2[N - 1])


def dp(start, end, sum_arr, sticker):
    for i in range(start, end):
        if i == start:
            sum_arr[i] = sticker[i]
        elif i == start + 1:
            sum_arr[i] = max(sum_arr[i - 1], sticker[i])
        else:
            sum_arr[i] = max(sum_arr[i - 2] + sticker[i], sum_arr[i - 1])
