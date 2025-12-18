def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return right - left - 1

    max_len = 1
    for i in range(len(s) - 1):
        max_len = max(max_len, expand(i, i), expand(i, i + 1))

    return max_len