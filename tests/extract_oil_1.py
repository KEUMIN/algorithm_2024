# 프로그래머스 - 석유 시추 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/250136
# 사용 알고리즘 : BFS
# 인사이트 : 컬럼마다 BFS에서 산출된 카운트를 더하는 것이 핵심, 컬럼을 중심으로 사고
from collections import deque


def solution(land):
    row = len(land)
    col = len(land[0])
    result = [0] * col

    visit = [[False] * col for _ in range(row)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def bfs(x, y):
        visit_col = set()
        visit[x][y] = True
        visit_col.add(y)
        queue = deque([(x, y)])
        tot_cnt = 1

        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in directions:
                mx = cur_x + dx
                my = cur_y + dy
                if 0 <= mx < row and 0 <= my < col:
                    if not visit[mx][my] and land[mx][my] != 0:
                        visit[mx][my] = True
                        queue.append((mx, my))
                        visit_col.add(my)
                        tot_cnt += 1

        for i in visit_col:
            result[i] += tot_cnt

    for j in range(col):
        for i in range(row):
            if land[i][j] != 0 and not visit[i][j]:
                bfs(i, j)

    return max(result)
