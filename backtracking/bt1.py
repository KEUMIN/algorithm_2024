# nums = [1,2,3,4]로 만들 수 있는 모든 순열을 반환하시오

def permute(nums):
    def backtracking(arr):
        if len(arr) == len(nums):
            result.append(arr[:])
            return
        
        for num in nums:
            if num not in arr:
                arr.append(num)
                backtracking(arr)
                arr.pop()
            
            
            
    result = []
    backtracking([])
    return result

print(permute(nums = [1,2,3,4]))