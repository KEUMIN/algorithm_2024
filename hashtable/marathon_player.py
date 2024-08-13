from collections import defaultdict

def solution(participant, completion):
    dict = defaultdict(int)
    for player in participant:
        dict[player] += 1
            
    for comp_player in completion:
        dict[comp_player] -= 1
        
    return next((k for k, v in dict.items() if v > 0))