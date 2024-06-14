from collections import deque

def visit_all_rooms(rooms):
    visited = [False] * len(rooms)
    visited[0] = True
    
    def dfs(keys):
        for room_num_of_key in keys:
            if not visited[room_num_of_key]:
                visited[room_num_of_key] = True
                dfs(rooms[room_num_of_key])
            
    dfs(rooms[0])
    
    return not False in visited
    

print(visit_all_rooms(rooms = [[1], [2], [3], []]))