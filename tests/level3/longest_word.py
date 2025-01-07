# 프로그래머스 - 가장 긴 팰린드롬 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/12904
# 사용 알고리즘 : ???
def solution(s):
    for n in range(len(s), 1, -1):
        mid = n // 2
        for i in range(len(s) - n + 1):
            if s[i : mid + i] == s[mid + i + n % 2 : mid * 2 + i + n % 2][::-1]:
                return n

    return 1


print(solution("abacde"))
