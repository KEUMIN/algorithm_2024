# 프로그래머스 - 기지국 설치 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/12979
# 사용 알고리즘 : 그리디


def solution(N, stations, W):
    answer = 0
    for i in range(len(stations) + 1):
        start = stations[i - 1] + W if i != 0 else 0
        end = stations[i] - W - 1 if i != len(stations) else N
        answer += (end - start) // (2 * W + 1)
        if (end - start) % (2 * W + 1) > 0:
            answer += 1
    return answer
