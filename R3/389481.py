from bisect import bisect_right


def get_sum(n):
    return (26 * ((26**n) - 1)) // (26 - 1) if n > 0 else 0


def idx_to_str(idx):
    L = 1
    while get_sum(L) < idx:
        L += 1

    pure_idx = idx - get_sum(L - 1) - 1
    arr = []
    for i in range(L - 1, -1, -1):
        arr.append(chr(ord("a") + pure_idx % 26))
        pure_idx //= 26

    arr.reverse()
    return "".join(arr)


def str_to_idx(s):
    L = len(s)
    idx = 0
    for c in s:
        idx = (idx * 26) + (ord(c) - ord("a"))

    return idx + get_sum(L - 1) + 1


def solution(n, bans):
    bans_idx = sorted([str_to_idx(b) for b in bans])
    left, right = 1, 10**15
    while left <= right:
        mid = (left + right) // 2
        kept = mid - bisect_right(bans_idx, mid)
        if kept >= n:
            right = mid - 1
        else:
            left = mid + 1

    return idx_to_str(left)
