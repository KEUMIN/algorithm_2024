def solution(n, cores):
    m = len(cores)
    if n <= m:
        return n

    # 이분 탐색: 처리 완료 시간을 최소화
    left, right = 1, max(cores) * n

    def processed(t):
        # 시간 t까지 진행된 작업 수
        return m + sum(t // c for c in cores)

    while left < right:
        mid = (left + right) // 2
        if processed(mid) >= n:
            right = mid
        else:
            left = mid + 1
    t = left  # t* (최소 시각)

    # 직전까지 끝난 작업 수
    prev = processed(t - 1)
    remain = n - prev  # t 시각에 끝난 코어들 중 앞에서부터 remain번째가 정답

    # 코어 번호가 작은 순서대로 확인
    for i, c in enumerate(cores):
        if t % c == 0:  # 이 코어가 t 시각에 막 끝남
            remain -= 1
            if remain == 0:
                return i + 1


print(solution(6, [1, 2, 3]))
