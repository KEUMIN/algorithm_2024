from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_score_diff = 0
    max_info = []

    def get_info(combi):
        info = [0] * 11
        for i in combi:
            info[10 - i] += 1
        return info 
    
    def get_score_diff(apeach_info, ryan_info):
        score_diff = 0
        
        for i in range(11):
            if ryan_info[i] > apeach_info[i]:
                score_diff += 10 - i
            elif apeach_info[i] > 0:
                score_diff -= 10 - i
                
        return score_diff
    
    def set_max(cur_score_diff, info):
        nonlocal max_score_diff
        nonlocal max_info
        
        # combination이 오름차순이기 때문에 추가조건인
        # 같을 경우 낮은 점수가 더 많은 쪽을 비교하는 것은 불필요하다.
        if cur_score_diff > max_score_diff:
            max_score_diff = cur_score_diff
            max_info = info
   
    for combi in combinations_with_replacement(range(11), n):
        ryan_info = get_info(combi)
        score_diff = get_score_diff(info, ryan_info)
        set_max(score_diff, ryan_info)

    return max_info if max_score_diff > 0 else [-1]