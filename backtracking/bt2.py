def solution(nums, k):
    result = []
    arr = []
    
    def backtracking(start, arr):
        if len(arr) == k and arr not in result:
            result.append(arr[:])
            return
        
        for i in range(start, len(nums)):
            arr.append(nums[i])
            backtracking(i+1, arr)
            arr.pop()
                
    backtracking(0, arr)
    return result


print(solution(nums =[1,2,3,4], k = 2))