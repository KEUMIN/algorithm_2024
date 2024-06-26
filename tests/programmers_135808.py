def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    for i in range(len(score)):
        if (i+1) % m == 0:
            answer += score[i]*m
    
    return answer

def other_solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))