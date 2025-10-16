# 맨해튼 + 파리티
def solution(n, m, x, y, r, c, k):
    # 1) 사전 불가능성 체크
    need = abs(x - r) + abs(y - c)
    if need > k or ((k - need) % 2) == 1:
        return "impossible"

    # 2) 사전순 시도 순서: d < l < r < u
    moves = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]

    path = []
    cx, cy = x, y  # 입력이 1-index이므로 그대로 사용
    for used in range(k):
        for ch, dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                rem = k - (used + 1)
                new_need = abs(nx - r) + abs(ny - c)
                # 남은 걸음으로 도달 가능 + 파리티 만족
                if new_need <= rem and ((rem - new_need) % 2) == 0:
                    path.append(ch)
                    cx, cy = nx, ny
                    break

    return "".join(path)
