dungeons = [[80,20],[50,40],[30,10]]
k = 80

def dfs(cur_k, dungeons, count, visited):
    result = count
    
    for i in range(len(dungeons)):
        if dungeons[i][0] <= cur_k and not visited[i]:
            visited[i] = True
            result = max(result, dfs(cur_k - dungeons[i][1], dungeons, count + 1, visited))
            visited[i] = False
            
    return result

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, 0, visited)

    
print(solution(k, dungeons))