def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    return max(get_max_from_dp(sticker[:-1]), get_max_from_dp(sticker[1:]))


def get_max_from_dp(arr):
    dp = [0] * len(arr)

    for i in range(len(arr)):
        if i == 0:
            dp[0] = arr[0]
        elif i == 1:
            dp[1] = max(dp[0], arr[1])
        else:
            dp[i] = max(dp[i - 1], (dp[i - 2] + arr[i]))

    return max(dp)