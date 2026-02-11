def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def check(x, y, M, N, key, expanded):
    for i in range(M):
        for j in range(M):
            expanded[x + i][y + j] += key[i][j]

    is_valid = all(
        expanded[i][j] == 1
        for i in range(M - 1, M - 1 + N)
        for j in range(M - 1, M - 1 + N)
    )

    for i in range(M):
        for j in range(M):
            expanded[x + i][y + j] -= key[i][j]

    return is_valid


def solution(key, lock):
    M, N = len(key), len(lock)

    size = N + 2 * (M - 1)
    expanded = [[0] * size for _ in range(size)]
    for i in range(N):
        for j in range(N):
            expanded[i + M - 1][j + M - 1] = lock[i][j]

    for _ in range(4):
        for x in range(size - M + 1):
            for y in range(size - M + 1):
                if check(x, y, M, N, key, expanded):
                    return True
        key = rotate(key)

    return False
