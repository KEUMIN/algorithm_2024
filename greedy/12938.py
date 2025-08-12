# def solution(n, s):
#     if n > s:
#         return [-1]
#
#     rem = s % n
#     quot = s // n
#     result = []
#
#     for _ in range(n):
#         num = quot
#         if rem > 0:
#             num += 1
#             rem -= 1
#         result.append(num)
#
#     return sorted(result)


def solution(n, s):
    # quotient : 몫 / reminder : 나머지
    quot, rem = divmod(s, n)
    if quot == 0:
        return [-1]
    return [quot] * (n - rem) + [quot + 1] * rem
