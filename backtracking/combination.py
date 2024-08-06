def solution(N):
    result = []
    def backtrack(sum, selected_nums, start):
        if sum == 10:
            result.append(selected_nums[:])
            return
        if sum > 10:
            return
        
        for i in range(start, N + 1):
            selected_nums.append(i)
            backtrack(sum + i, selected_nums, i + 1)
            selected_nums.pop()
            
    backtrack(0, [], 1)
    return result

print(solution(10))