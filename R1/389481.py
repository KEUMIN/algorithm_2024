from bisect import bisect_right

NUM_OF_ALP = 26


def get_sum(num):
    return (NUM_OF_ALP * (NUM_OF_ALP**num - 1)) // (NUM_OF_ALP - 1) if num > 0 else 0


def idx_of(s):
    L = len(s)
    v = 0
    for ch in s:
        v = v * 26 + (ord(ch) - 97)
    pos_within_len = v + 1
    return get_sum(L - 1) + pos_within_len


def str_at_idx(x):
    L = 1
    while get_sum(L) < x:
        L += 1
    off = x - get_sum(L - 1) - 1
    arr = []
    for i in range(L - 1, -1, -1):
        arr.append(chr(97 + (off % 26)))
        off //= 26
    arr.reverse()
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
