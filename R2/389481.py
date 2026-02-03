from bisect import bisect_right


def get_sum(i):
    return (26 * (26**i - 1)) // (26 - 1) if i > 0 else 0


def get_str_from_idx(idx):
    i = 1
    while get_sum(i) < idx:
        i += 1
    remains = idx - get_sum(i - 1) - 1
    arr = []
    while remains > 0:
        arr.append(chr(ord("a") + (remains % 26)))
        remains = remains // 26
        i -= 1

    while i > 0:
        arr.append("a")
        i -= 1

    arr.reverse()
    return "".join(arr)


def get_idx_from_str(string):
    tmp = 0
    for c in string:
        tmp = tmp * 26 + ord(c) - ord("a")

    return tmp + 1 + get_sum(len(string) - 1)


def solution(n, bans):
    bans_idx = sorted([get_idx_from_str(b) for b in bans])
    left, right = 1, 10**15
    while left <= right:
        mid = (left + right) // 2
        removed = bisect_right(bans_idx, mid)
        kept = mid - removed
        if kept >= n:
            right = mid - 1
        else:
            left = mid + 1

    return get_str_from_idx(left)
