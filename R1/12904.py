def solution(s):
    result = 1
    for i, c in enumerate(s):
        l1, r1 = i, i
        l2, r2 = i, i + 1
        cnt1, cnt2 = 1, 1

        while 0 <= l1 and r1 < len(s) and s[l1] == s[r1]:
            cnt1 = r1 - l1 + 1
            l1 -= 1
            r1 += 1

        while 0 <= l2 and r2 < len(s) and s[l2] == s[r2]:
            cnt2 = r2 - l2 + 1
            l2 -= 1
            r2 += 1

        result = max(result, cnt1, cnt2)

    return result


solution("abcdcba")