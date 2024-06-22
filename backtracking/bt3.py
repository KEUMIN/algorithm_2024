def n_sum(nums, k, target):
    surr = []
    result = False
    
    def backtracking(start, surr):
        result = False
        
        if len(surr) == k:
            if sum(surr) == target:
                return True
            else:
                return
        
        for i in range(start, len(nums)):
            surr.append(nums[i])
            result = backtracking(i + 1, surr)
            if result:
                return True
            surr.pop()
            
    result = backtracking(0, surr)
    return result


print(n_sum(nums=[4,9,7,5,1,3], k=4, target=13))