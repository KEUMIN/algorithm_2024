def solution(cards):
    visit = []
    num = []
    cnt = 0
    
    def dfs(n, num):
        nonlocal cnt
        if cards[n-1] not in visit:
            cnt += 1
            visit.append(cards[n-1])
            dfs(cards[n-1], num)
        else:
            num.append(cnt)
            cnt = 0
            
    for i in range(len(cards)):
        if cards[i] not in visit:
            dfs(i + 1, num)
            
    if num[0] == len(cards):
        return 0
    else:
        num.sort(reverse=True)
        return num[0] * num[1]

solution([8,6,3,7,2,5,1,4])