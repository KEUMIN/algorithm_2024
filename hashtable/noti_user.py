# 프로그래머스 92334
from collections import defaultdict

def solution(id_list, report, k):
    noti_cnt = defaultdict(int)
    user_noti = defaultdict(list)
    
    for rep in report:
        id_n_target = rep.split(" ")
        id = id_n_target[0]
        target = id_n_target[1]
        if target not in user_noti[id]:
            user_noti[id].append(target)
            noti_cnt[target] += 1
    result = []
    for id in id_list:
        cnt = 0
        for target in user_noti[id]:
            if noti_cnt[target] >= k:
                cnt += 1
        result.append(cnt)
    return result