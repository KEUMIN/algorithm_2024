# 프로그래머스 - 입국 심사 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 사용 알고리즘 : 이진 탐색 - 범위가 말도 안되게 클 때 일단 이진 탐색 시도해보기
def solution(n, times):
    # 최소 시간과 최대 시간 설정
    left = min(times)  # 최소 시간
    right = max(times) * n  # 최대 시간

    # 이진 탐색 시작
    while left <= right:
        mid = (left + right) // 2
        people = 0  # 심사 가능한 사람 수

        # 주어진 시간(mid)동안 각 심사관이 처리할 수 있는 사람 수 계산
        for time in times:
            people += mid // time

            # 모든 심사관을 확인하기 전에 n명을 넘어서면 반복 중단
            if people >= n:
                break

        # n명을 처리할 수 있는 경우
        if people >= n:
            answer = mid
            right = mid - 1  # 더 작은 시간에서 가능한지 확인
        # n명을 처리할 수 없는 경우
        else:
            left = mid + 1  # 더 큰 시간이 필요

    return answer
