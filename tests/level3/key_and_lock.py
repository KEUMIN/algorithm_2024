# 프로그래머스 - 자물쇠와 열쇠 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/60059
# 사용 알고리즘 : 시뮬레이션 & 브루트 포스


def solution(key, lock):
    M = len(key)
    N = len(lock)

    for _ in range(4):
        key = rotate(key)
        if any(
            check(key, lock, M, N, i, j) for j in range(N * 2) for i in range(N * 2)
        ):
            return True
    return False


def check(key, lock, M, N, x, y):
    temp = [[0] * N * 3 for _ in range(N * 3)]
    for i in range(N):
        temp[N + i][N : N * 2] = lock[i]

    for i in range(M):
        for j in range(M):
            temp[i + x][j + y] += key[i][j]

    return all(temp[i + N][j + N] == 1 for j in range(N) for i in range(N))


def rotate(key):
    return list(zip(*key[::-1]))
