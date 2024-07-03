targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	

def solution(targets):
    # 종료점을 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    # 요격 미사일의 수
    missile_count = 0
    
    # 마지막 요격 미사일이 발사된 위치
    last_intercept = -float('inf')
    
    for s, e in targets:
        # 현재 폭격 미사일의 시작점이 마지막 요격 미사일의 위치보다 큰 경우
        if s >= last_intercept:
            # 새로운 요격 미사일을 발사
            last_intercept = e
            missile_count += 1
    
    return missile_count
    
    
print(solution(targets))
        