# def solution(user_id, banned_id):
#     def match(u, p):
#         return len(u) == len(p) and all(pc == "*" or uc == pc for uc, pc in zip(u, p))
#
#     # 각 불량 패턴에 매칭 가능한 user 인덱스 목록
#     cand = [[i for i, u in enumerate(user_id) if match(u, p)] for p in banned_id]
#
#     ans = set()
#
#     def dfs(k, mask):
#         if k == len(cand):
#             ans.add(mask)
#             return
#         for i in cand[k]:
#             if not (mask >> i) & 1:
#                 dfs(k + 1, mask | (1 << i))
#
#     dfs(0, 0)
#     return len(ans)


from functools import reduce
import re


def solution(user_id, banned_id):
    banned_patterns = [re.compile(bid.replace("*", ".")) for bid in banned_id]
    candidates = [
        {uid for uid in user_id if pattern.fullmatch(uid)}
        for pattern in banned_patterns
    ]

    # result_set = reduce(
    #     lambda acc, candidate: {
    #         selected | {user}
    #         for selected in acc
    #         for user in candidate
    #         if user not in selected
    #     },
    #     candidates,
    #     {frozenset()},
    # )

    result_set = set()  # frozenset 묶음 보관
    chosen = set()  # 진행 중 선택 집합 (가변, 백트래킹)

    def dfs(k: int):
        if k == len(candidates):
            result_set.add(frozenset(chosen))
            return
        for u in candidates[k]:
            if u in chosen:
                continue
            chosen.add(u)
            dfs(k + 1)
            chosen.remove(u)

    dfs(0)
    return len(result_set)


print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    )
)
