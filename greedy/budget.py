#12982 예산
def solution(d, budget):
    moneys = sorted(d)
    cnt = 0
    for money in moneys:
        if budget >= money:
            cnt += 1
            budget -= money
        else:
            break
    return cnt