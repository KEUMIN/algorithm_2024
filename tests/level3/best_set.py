# 프로그래머스 - 최고의 집합 : https://school.programmers.co.kr/learn/courses/30/lessons/12938
# 사용 알고리즘 : 그리디


def solution(n, s):
    if n > s:
        return [-1]

    answer = [(s // n)] * n
    for i in range(s % n):
        answer[n - i - 1] += 1

    return answer
