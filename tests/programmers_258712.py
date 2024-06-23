def solution(friends, gift):
    f_idx = {v:i for i, v in enumerate(friends)}
    answer = 0
    num_of_friends = len(friends)
    graph = [[0] * num_of_friends for _ in range(num_of_friends)]    
    gift_records = []
    
    for gift in gifts:
        g, r = gift.split()
        graph[f_idx[g]][f_idx[r]] += 1
        
    for i in range(num_of_friends):
        gift_records.append(sum(graph[i]) - sum(k[i] for k in graph))
        
    for i in range(num_of_friends):
        num_of_next_month = 0
        
        for j in range(num_of_friends):
            if i == j:
                continue
            if graph[i][j] == graph[j][i] or graph[i][j] == 0 and graph[j][i] == 0:
                if gift_records[i] > gift_records[j]:
                    num_of_next_month += 1
                
            else:
                if graph[i][j] > graph[j][i]:
                    num_of_next_month += 1
            
        answer = max(answer, num_of_next_month)
        
    
    return answer
    
      

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends, gifts))