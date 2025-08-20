# 처음 내 풀이
def solution0(gems):
    s, e = 0, 1
    gs = set()
    for g in gems:
        gs.add(g)

    if len(gs) == 1:
        return [1, 1]

    MAX_LEN = 100000
    result = [1, len(gems)]

    gc = dict()
    gc[gems[0]] = 1

    while e < len(gems):
        if gems[e] not in gc:
            gc[gems[e]] = 1
        else:
            gc[gems[e]] += 1
        e += 1

        while gc[gems[s]] > 1:
            gc[gems[s]] -= 1
            s += 1

        cur_len = e - s + 1
        if len(gs) == len(gc.keys()) and cur_len < MAX_LEN and e < result[1]:
            MAX_LEN = cur_len
            result = [s + 1, e]

    return result


# 수정
from collections import defaultdict


def solution(gems):
    total_kinds = len(set(gems))
    count = defaultdict(int)

    best_start, best_end = 0, len(gems) - 1
    s = 0

    for e, g in enumerate(gems):
        count[g] += 1
        # 모든 종류를 포함하면 왼쪽을 최대한 줄이기
        while len(count) == total_kinds and s <= e:
            # 현재 윈도우 [s, e] 길이 비교
            if (e - s) < (best_end - best_start):
                best_start, best_end = s, e

            # s를 한 칸 밀며 카운트/종류 갱신
            left = gems[s]
            count[left] -= 1
            if count[left] == 0:
                del count[left]
            s += 1

    return [best_start + 1, best_end + 1]
