# 프로그래머스 - 스티커 모으기 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/12971
# 사용 알고리즘 : DP
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    dp1 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], sticker[0]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    dp2 = [0] * len(sticker)
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[-2], dp2[-1])
