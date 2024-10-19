# 프로그래머스 - 혼자 놀기의 달인 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/131130
# 사용 알고리즘 : BFS,DFS
from collections import deque


def solution(cards):
    visit = [False] * len(cards)
    groups = []

    def bfs(index):
        visit[index] = True
        queue = deque([cards[index] - 1])
        cnt = 1

        while queue:
            cur_idx = queue.popleft()
            if not visit[cur_idx]:
                visit[cur_idx] = True
                queue.append(cards[cur_idx] - 1)
                cnt += 1

        return cnt

    for i in range(len(cards)):
        if not visit[i]:
            groups.append(bfs(i))

    groups = sorted(groups, reverse=True)

    return groups[0] * groups[1] if len(groups) > 1 else 0
