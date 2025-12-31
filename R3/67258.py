from collections import defaultdict


def solution(gems):
    N = len(gems)
    types = len(set(gems))

    if types == 1:
        return [1, 1]

    gem_map = defaultdict(int)
    min_length = N
    min_range = [1, N]
    left = 0
    mem_set = set()

    gem_map[gems[left]] += 1
    mem_set.add(gems[left])

    for i in range(1, N):
        gem_map[gems[i]] += 1
        mem_set.add(gems[i])
        while len(mem_set) == types:
            if i - left + 1 < min_length:
                min_length = i - left + 1
                min_range = [left + 1, i + 1]
            gem_map[gems[left]] -= 1

            if gem_map[gems[left]] == 0:
                mem_set.remove(gems[left])

            left += 1

    return min_range
