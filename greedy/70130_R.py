from collections import Counter


def solution(a):
    N = len(a)
    if N < 4:
        return 0

    freq = Counter(a)
    best = 0

    for v, cnt in freq.items():
        if cnt * 2 <= best:
            continue

        # 내가 생각 못한 부분 - 시작
        pairs = 0
        i = 0
        while i < N - 1:
            # 같은 값끼리 붙은 구간은 쌍을 만들 수 없음
            if a[i] == a[i + 1]:
                i += 1
                continue

            # 서로 다른 인접한 두 값 중 하나가 v이면 유효 쌍
            if a[i] == v or a[i + 1] == v:
                pairs += 1
                i += 2  # 이 두 원소로 한 쌍을 사용
            else:
                i += 1

        best = max(best, pairs * 2)
        # 내가 생각 못한 부분 - 끝

    return best


solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0])
