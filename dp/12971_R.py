def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker)

    def max_sum(arr):
        dp = [0] * len(arr)
        dp[0], dp[1] = arr[0], max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
        return dp[-1]

    return max(max_sum(sticker[:-1]), max_sum(sticker[1:]))
