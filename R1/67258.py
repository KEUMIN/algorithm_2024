# 오답: 슬라이딩 윈도우는 양 끝단에서 시작하며, 가장 짧은 구간을 택하는게 아니라 처음부터 모든 보석을 포함하는 구간을 구하는 우를 범함
from collections import defaultdict


def solution(gems):
    N = len(set(gems))
    if N == 1:
        return [1, 1]

    start = 0
    end = 0
    gem_map = defaultdict(int)
    gem_map[gems[0]] += 1

    while len(gem_map.keys()) != N:
        end += 1
        gem_map[gems[end]] += 1

        while gem_map[gems[start]] > 1:
            gem_map[gems[start]] -= 1
            start += 1

    return [start + 1, end + 1]