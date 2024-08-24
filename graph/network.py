from collections import deque

def solution(n, computers):
    visited = set()
    
    def bfs(start):
        visited.add(start)
        queue = deque([start])
        while queue:
            cur_node = queue.popleft()
            for neighbor, is_connected in enumerate(computers[cur_node]):
                if neighbor not in visited and is_connected != 0:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return 1
    
    result = 0
    for i in range(n):
        if i not in visited:
            result += bfs(i)
            
    return result