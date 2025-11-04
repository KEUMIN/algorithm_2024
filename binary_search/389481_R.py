from bisect import bisect_right

# 26^i, 길이 누적 개수(prefix): prefix[L] = 길이 1..L까지 총 개수
POW26 = [1]
for _ in range(11):
    POW26.append(POW26[-1] * 26)
# prefix[0]=0, prefix[L]=sum_{i=1..L} 26^i
PREFIX = [0]
for L in range(1, 12):
    PREFIX.append(PREFIX[-1] + POW26[L])


def idx_of(s):
    """문자열 s의 '전체 목록(삭제 전)' 1-base 인덱스"""
    L = len(s)
    v = 0
    for ch in s:
        v = v * 26 + (ord(ch) - 97)  # 'a'->0, ... 'z'->25
    pos_within_len = v + 1  # 길이 L 내에서 1-base
    return PREFIX[L - 1] + pos_within_len


def str_at_idx(x):
    """전체 목록(삭제 전)에서 1-base 인덱스 x에 해당하는 문자열"""
    # 길이 결정: PREFIX[L-1] < x <= PREFIX[L]
    L = 1
    while PREFIX[L] < x:
        L += 1
    off = x - PREFIX[L - 1] - 1  # 길이 L 내 0-base 오프셋
    # off를 26진수로 L자리(앞쪽 0 허용)로 변환
    arr = ["a"] * L
    for i in range(L - 1, -1, -1):
        arr[i] = chr(97 + (off % 26))
        off //= 26
    return "".join(arr)


def solution(n, bans):
    banned_idx = [idx_of(b) for b in bans]
    banned_idx.sort()

    lo, hi = 1, 10**15
    while lo < hi:
        mid = (lo + hi) // 2
        removed = bisect_right(banned_idx, mid)
        kept = mid - removed
        if kept >= n:
            hi = mid
        else:
            lo = mid + 1

    return str_at_idx(lo)
