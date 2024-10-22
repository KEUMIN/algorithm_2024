# 프로그래머스 - 가장 많이 받은 선물 (LV1) : https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 사용 알고리즘 : 내 풀이 (완전 탐색(브루트 포스) + 해시) / 오리지날 풀이 (완전 탐색(브루트 포스) + 인접 행렬)
from itertools import combinations


def solution(friends, gifts):
    give_take = {}
    next_month_gifts = {}
    givers = [rec.split()[0] for rec in gifts]
    takers = [rec.split()[1] for rec in gifts]

    for friend in friends:
        give_take[friend] = {}
        next_month_gifts[friend] = 0

    for record in gifts:
        giver, taker = record.split()
        if taker not in give_take[giver]:
            give_take[giver][taker] = 1
        else:
            give_take[giver][taker] += 1

    def gift_for_more_gift_point(combi):
        a, b = combi
        a_point = givers.count(a) - takers.count(a)
        b_point = givers.count(b) - takers.count(b)

        if a_point > b_point:
            next_month_gifts[a] += 1
        elif b_point > a_point:
            next_month_gifts[b] += 1

    def gift_for_more_giver(combi):
        a, b = combi
        a_give = give_take[a][b] if b in give_take[a] else 0
        b_give = give_take[b][a] if a in give_take[b] else 0
        if a_give > b_give:
            next_month_gifts[a] += 1
        elif b_give > a_give:
            next_month_gifts[b] += 1
        else:
            gift_for_more_gift_point(combi)

    for combi in combinations(friends, 2):
        gift_for_more_giver(combi)

    return max(next_month_gifts.values())


def original_solution(friends, gifts):
    f_idx = {v: i for i, v in enumerate(friends)}
    answer = 0
    num_of_friends = len(friends)
    graph = [[0] * num_of_friends for _ in range(num_of_friends)]
    gift_records = []

    for gift in gifts:
        g, r = gift.split()
        graph[f_idx[g]][f_idx[r]] += 1

    for i in range(num_of_friends):
        gift_records.append(sum(graph[i]) - sum(k[i] for k in graph))

    for i in range(num_of_friends):
        num_of_next_month = 0

        for j in range(num_of_friends):
            if i == j:
                continue
            if graph[i][j] == graph[j][i] or graph[i][j] == 0 and graph[j][i] == 0:
                if gift_records[i] > gift_records[j]:
                    num_of_next_month += 1

            else:
                if graph[i][j] > graph[j][i]:
                    num_of_next_month += 1

        answer = max(answer, num_of_next_month)

    return answer
