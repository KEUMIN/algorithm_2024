from collections import deque


def solution(n, m, x, y, r, c, k):
    dir_dict = {"d": (1, 0), "l": (0, -1), "r": (0, 1), "u": (-1, 0)}
    dir_list = ["d", "l", "r", "u"]

    result_arr = []

    queue = deque([(x - 1, y - 1, 0, "")])

    while queue:
        cx, cy, dist, path = queue.popleft()

        if dist == k:
            if cx == r - 1 and cy == c - 1:
                result_arr.append(path)
                continue
            else:
                continue

        for d in dir_list:
            dx, dy = dir_dict[d][0], dir_dict[d][1]
            mx, my = cx + dx, cy + dy
            if 0 <= mx < n and 0 <= my < m:
                queue.append((mx, my, dist + 1, path + d))

    return result_arr[0] if len(result_arr) != 0 else "impossible"
