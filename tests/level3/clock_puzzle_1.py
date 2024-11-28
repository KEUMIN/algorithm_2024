def solution(clockHands):
    answer = 0
    for i in range(1, len(clockHands)):
        for j in range(len(clockHands)):
            answer += rotate(clockHands, i, j)

    return answer


def rotate(clockHands, x, y):
    if clockHands[x - 1][y] == 0:
        return 0
    else:
        cnt = 0
        while clockHands[x - 1][y] > 0:
            cnt += 1
            d = [(0, 0), (1, 0), (0, -1), (-1, 0), (0, 1)]
            for dx, dy in d:
                mx, my = (x + dx), (y + dy)
                if 0 <= mx < len(clockHands) and 0 <= my < len(clockHands):
                    clockHands[mx][my] = (clockHands[mx][my] + 1) % 4
        return cnt
