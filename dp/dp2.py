    
def climb_min_cost(cost):
    memo = {}
    idx = len(cost)

    def min_cost(idx):
        if idx == 0 or idx == 1:
            return 0
                
        if idx not in memo:
            memo[idx] = min((cost[idx - 1] + min_cost(idx - 1)), (cost[idx - 2] + min_cost(idx - 2)))
        
        return memo[idx]
    
    return min_cost(idx)


print(climb_min_cost(cost = [10, 15, 20, 17, 1]))