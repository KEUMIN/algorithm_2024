def two_sum(input, target):
    dic = {}
    
    for i in input:
        dic[i] = True
        
    for i in input:
        sub = target - i
        if sub in dic:
            return True
        
    return False


input = [4, 5, 7, 12, 9]
target = 14

print(two_sum(input, target))
