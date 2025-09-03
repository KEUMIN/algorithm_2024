from collections import defaultdict


def solution(enroll, referral, seller, amount):
    r_map = {}
    i_map = defaultdict(int)
    for i in range(len(enroll)):
        r_map[enroll[i]] = referral[i]

    def dfs(worker, income):
        if worker == "-":
            return
        commission = income // 10
        if (commission) >= 1:
            i_map[worker] += income - commission
            dfs(r_map[worker], commission)
        else:
            i_map[worker] += income

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)

    return [i_map[w] for w in enroll]
