# 프로그래머스 - 고고학 최고의 발견 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/131702
# 사용 알고리즘 : 브루트 포스, 그리디
# 인사이트 : - n진수 x의 각 자리(y) 구하는 공식 : (x // n**y) % n
#          - 한 행의 시계 회전 결과는 결국 최종적으로 동일하다. 순서는 상관 없음(시계회전의 교환 법칙)
def solution(clockHands):
    n = len(clockHands)
    min_op = float("inf")

    def rotate(x, y, clock, cnt):
        d = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in d:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                clock[nx][ny] = (clock[nx][ny] + cnt) % 4

    def check_rotated(clock):
        return all(clock[n - 1][j] % 4 == 0 for j in range(n))

    for fst_row_state in range(4**n):
        tmp_clock = [row[:] for row in clockHands]
        op = 0

        for j in range(n):
            rotations = (fst_row_state // 4**j) % 4
            if rotations > 0:
                rotate(0, j, tmp_clock, rotations)
                op += rotations

        for i in range(1, n):
            for j in range(n):
                # 위의 시계를 0으로 만드는 회전 횟수
                rotations = (4 - tmp_clock[i - 1][j]) % 4
                if rotations > 0:
                    rotate(i, j, tmp_clock, rotations)
                    op += rotations

        if check_rotated(tmp_clock):
            min_op = min(min_op, op)

    return min_op
