# 프로그래머스 - 신고 결과 받기(LV1) : https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 사용 알고리즘 : 해시
from collections import defaultdict


def solution(id_list, report, k):
    complains = defaultdict(set)
    for rep in report:
        user, target = rep.split()
        complains[user].add(target)

    black_users = defaultdict(int)
    for users in complains.values():
        for user in users:
            black_users[user] += 1

    banned_user = [user for user, num in black_users.items() if num >= k]

    result = [0 for _ in range(len(id_list))]
    for i in range(len(id_list)):
        for b in banned_user:
            if b in complains[id_list[i]]:
                result[i] += 1

    return result
