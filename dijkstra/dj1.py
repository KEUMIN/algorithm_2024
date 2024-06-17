import heapq
from collections import defaultdict

times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]]

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1]))
    
    costs = {}
    heap = []
    heapq.heappush(heap, (0, k))
    
    while heap:
        cur_cost, cur_v = heapq.heappop(heap)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(heap, (next_cost, next_v))
                
    for v in range(1, n + 1):
        if v not in costs:
            return -1
        
    return max(costs.values())            
            
print(network_delay_time(times, 4, 2))