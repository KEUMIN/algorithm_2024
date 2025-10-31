# 패리티 (parity) 문제로 가능성을 좁혀서 생각하는 게 관건
def solution(beginning, target):
    R, C = len(beginning), len(beginning[0])

    # 1) D = beginning XOR target
    D = [[beginning[i][j] ^ target[i][j] for j in range(C)] for i in range(R)]

    INF = 10**9
    answer = INF

    # 2) 모든 "행 뒤집기" 경우(비트마스크) 시도
    for mask in range(1 << R):
        # 2-1) 현재 mask에 따라 행을 뒤집은 결과를 만든다
        #      row_flipped[i] == 1 이면 i번째 행의 모든 비트를 뒤집은 것으로 간주
        after_rows = []
        for i in range(R):
            if (mask >> i) & 1:  # i행을 뒤집기
                after_rows.append([1 - v for v in D[i]])
            else:
                after_rows.append(D[i][:])

        # 2-2) 열을 확인: 각 열이 전부 0이거나 전부 1이어야 가능
        col_flips = 0
        possible = True
        for j in range(C):
            col_vals = [after_rows[i][j] for i in range(R)]
            ones = sum(col_vals)
            if ones == 0:
                # 이 열은 그대로 두면 됨
                continue
            elif ones == R:
                # 이 열은 한 번 뒤집으면 0열이 됨
                col_flips += 1
            else:
                # 섞여 있으면 어떤 열 뒤집기로도 전부 0으로 못 만든다
                possible = False
                break

        if possible:
            flips = bin(mask).count("1") + col_flips  # 행 뒤집기 수 + 열 뒤집기 수
            answer = min(answer, flips)

    return -1 if answer == INF else answer
