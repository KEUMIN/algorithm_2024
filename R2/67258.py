from collections import defaultdict


def solution(gems):
    total_types = len(set(gems))
    gem_count = defaultdict(int)
    current_types = 0

    left = 0
    min_len = len(gems)
    answer = [1, len(gems)]

    for right in range(len(gems)):
        if gem_count[gems[right]] == 0:
            current_types += 1
        gem_count[gems[right]] += 1

        while current_types == total_types:
            if right - left < min_len:
                min_len = right - left
                answer = [left + 1, right + 1]

            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                current_types -= 1
            left += 1

    return answer
