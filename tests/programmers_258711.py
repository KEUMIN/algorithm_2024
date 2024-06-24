def solution(edges):
    answer = [0] * 4
    io = {}
    for e in edges:
        f, t = e
        if f not in io:
            io[f] = [0, 0]
        if t not in io:
            io[t] = [0, 0]
        io[f][1] += 1
        io[t][0] += 1 
    
    for k, v in io.items():
        if v[1] >= 2:
            if v[0] == 0:
                answer[0] = k
            else:
                answer[3] += 1
        elif v[1] == 0 and v[0] > 0:
            answer[2] += 1
            
    answer[1] = io[answer[0]][1] - (answer[2] + answer[3])
    
    return answer