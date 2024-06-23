def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends) # 친구 수
    p = [0] * l # 선물 지수
    answer = [0] * l
    gr = [[0] * l for i in range(l)] # 선물 그래프
    for i in gifts:
        a, b = i.split()
        gr[f[a]][f[b]] += 1
    
    # 선물 지수 초기화
    for i in range(l):
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])

    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)