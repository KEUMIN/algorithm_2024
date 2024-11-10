# 프로그래머스 - 입국 심사 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 사용 알고리즘 : 이진 탐색
def solution(n, times):
    times.sort()
    left = times[0]
    right = times[len(times) - 1] * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for t in times:
            if people >= n:
                break
            people += mid // t

        if people >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer
