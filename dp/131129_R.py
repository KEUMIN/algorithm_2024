def solution(target: int):
    # 가능한 점수(불=50 포함)와 "싱글/불로도 만들 수 있나" 플래그 구성
    flag = {}
    for n in range(1, 21):
        flag[n] = 1  # 싱글
        flag[2 * n] = max(flag.get(2 * n, 0), 0)  # 더블
        flag[3 * n] = max(flag.get(3 * n, 0), 0)  # 트리플
    flag[50] = 1  # 불(싱글 취급)
    scores = sorted(flag.keys())

    INF = 10**9
    dp = [(0, 0)] + [(INF, -INF)] * target  # (던진 횟수 최소, 싱글/불 횟수 최대)

    for s in range(1, target + 1):
        best = (INF, -INF)
        for v in scores:
            if v > s:
                break
            d, sb = dp[s - v]
            cand = (d + 1, sb + flag[v])
            if cand[0] < best[0] or (cand[0] == best[0] and cand[1] > best[1]):
                best = cand
        dp[s] = best

    return [dp[target][0], dp[target][1]]
