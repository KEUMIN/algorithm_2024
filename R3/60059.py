def rotate(matrix):
    return [list(r) for r in zip(*matrix[::-1])]


def check(key, expanded_lock, start_x, start_y, key_len, lock_len):
    for i in range(key_len):
        for j in range(key_len):
            expanded_lock[i + start_x][j + start_y] += key[i][j]

    is_valid = all(
        expanded_lock[i][j] == 1
        for i in range(key_len - 1, key_len + lock_len - 1)
        for j in range(key_len - 1, key_len + lock_len - 1)
    )

    for i in range(len(key)):
        for j in range(len(key)):
            expanded_lock[i + start_x][j + start_y] -= key[i][j]

    return is_valid


def solution(key, lock):
    M = len(key)
    N = len(lock)
    size = N + (M - 1) * 2

    expanded = [[0] * size for _ in range(size)]
    for i in range(N):
        for j in range(N):
            expanded[i + M - 1][j + M - 1] = lock[i][j]

    for _ in range(4):
        for i in range(size - M + 1):
            for j in range(size - M + 1):
                if check(key, expanded, i, j, M, N):
                    return True
        key = rotate(key)

    return False
