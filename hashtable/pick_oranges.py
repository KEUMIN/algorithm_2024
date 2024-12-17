from collections import defaultdict


def solution(k, tangerine):
    t_dict = defaultdict(int)
    for t in tangerine:
        t_dict[t] += 1

    t_list = []
    for key, value in t_dict.items():
        t_list.append((key, value))

    answer = 0
    to_pick = k

    for t in sorted(t_list, key=lambda x: x[1], reverse=True):
        answer += 1
        if to_pick <= t[1]:
            return answer
        to_pick -= t[1]
