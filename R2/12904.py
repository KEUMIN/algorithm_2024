def solution(s):
    max_len = 1
    for i in range(len(s)):
        len1 = expand(i, i, s)
        len2 = expand(i, i + 1, s)
        max_len = max(max_len, len1, len2)

    return max_len


def expand(l, r, s):
    left = l
    right = r
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
