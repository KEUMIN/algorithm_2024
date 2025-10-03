def solution(key, lock):
    M = len(key)
    N = len(lock)
    cur_key = key

    for _ in range(4):
        cur_key = get_rotate(cur_key)

        for x in range(2 * M):
            for y in range(2 * M):
                x_lock = [[-1] * (3 * N) for _ in range(3 * N)]
                for i in range(N):
                    for j in range(N):
                        x_lock[i + N][j + N] = lock[i][j]

                for i in range(M):
                    for j in range(M):
                        x_lock[N + 1 - M + x + i][N + 1 - M + y + j] += cur_key[i][j]

                if can_be_opened(x_lock, N): return True

    return False


def get_rotate(key):
    M = len(key)
    m_key = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            m_key[i][j] = key[M -1 -j][i]

    return m_key


def can_be_opened(lock, N):
    for i in range(N):
        for j in range(N):
            if lock[i + N][j + N] != 1:
                return False
    return True