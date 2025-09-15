def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    # 직사각형 차분 마킹
    for t, r1, c1, r2, c2, d in skill:
        s = -d if t == 1 else d
        diff[r1][c1] += s
        diff[r1][c2 + 1] -= s
        diff[r2 + 1][c1] -= s
        diff[r2 + 1][c2 + 1] += s

    # 가로 누적
    for i in range(n):
        run = 0
        row = diff[i]
        for j in range(m):
            run += row[j]
            row[j] = run

    # 세로 누적
    for j in range(m):
        run = 0
        for i in range(n):
            run += diff[i][j]
            diff[i][j] = run

    # 최종 적용 후 파괴되지 않은(>=1) 개수
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                ans += 1
    return ans
