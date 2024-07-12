from itertools import combinations
from itertools import chain

def get_wins(a, b, n):
    a.sort(reverse = True)
    b.sort(reverse = True)
    
    a_sums = []
    b_sums = []

    for a_comb in combinations(a, n):
        a_sums.append(sum(a_comb))
    for b_comb in combinations(b, n):
        b_sums.append(sum(b_comb))
        
    wins = 0
    for a_sum in a_sums:
        tmp = len(a_sums)
        for b_sum in b_sums:
            if b_sum < a_sum:
                break
            else:
                tmp -= 1
        wins += tmp
    return wins

def choice(dices, num):
    for comb in combinations(range(len(dices)), num):
        first_comb = [dices[i] for i in comb]
        a = list(chain.from_iterable(first_comb))
        
        remain_comb = [dices[i] for i in range(len(dices)) if i not in comb]
        b = list(chain.from_iterable(remain_comb))
        
        yield a, b, comb
        
def solution(dices):
    max_win = 0
    answer = []
    num = int(len(dices) / 2)
    
    for a, b, indices in choice(dices, num):
        tmp_wins = get_wins(a, b, num)
        if tmp_wins > max_win:
            max_win = tmp_wins
            answer = [x + 1 for x in indices]            
    return answer
        
dices = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
print(solution(dices))