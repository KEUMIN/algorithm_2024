# 프로그래머스 - 단어 변환 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 사용 알고리즘 : BFS
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [False] * len(words)
    queue = deque([(begin, 0)])

    while queue:
        source, cnt = queue.popleft()
        if source == target:
            return cnt

        for i in range(len(words)):
            if can_change(source, words[i]) and not visit[i]:
                queue.append((words[i], cnt + 1))
                visit[i] = True


def can_change(source, target):
    dif_cnt = 0
    for i in range(len(source)):
        if dif_cnt > 1:
            return False

        if source[i] != target[i]:
            dif_cnt += 1

    return True if dif_cnt == 1 else False
