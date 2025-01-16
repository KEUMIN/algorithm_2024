# 프로그래머스 - 풍선 터트리기 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/68646
# 사용 알고리즘 : 누적 최솟값(어려움: *****)
def solution(a):
    n = len(a)
    if n <= 2:  # 풍선이 2개 이하라면 모두 생존 가능
        return n

    left_min = [0] * n
    right_min = [0] * n

    # 왼쪽에서 최소값 누적
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    # 오른쪽에서 최소값 누적
    right_min[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    # 생존 가능한 풍선 개수 계산
    count = 0
    for i in range(n):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            count += 1

    return count
