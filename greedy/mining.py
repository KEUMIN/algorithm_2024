def solution(picks, minerals):
    # 곡괭이의 총 개수
    total_picks = sum(picks)

    # 광물을 5개씩 그룹화
    mineral_groups = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]

    # 사용 가능한 곡괭이 수만큼만 광물 그룹 고려
    mineral_groups = mineral_groups[:total_picks]

    # 각 그룹의 가치 계산 (다이아몬드 곡괭이로 캘 때의 피로도)
    def group_value(group):
        value = 0
        for mineral in group:
            if mineral == 'diamond':
                value += 25
            elif mineral == 'iron':
                value += 5
            else:
                value += 1
        return value

    # 그룹을 가치에 따라 정렬
    sorted_groups = sorted(mineral_groups, key=group_value, reverse=True)

    # 피로도 계산
    fatigue = 0
    for group in sorted_groups:
        if picks[0] > 0:  # 다이아몬드 곡괭이
            picks[0] -= 1
            for mineral in group:
                fatigue += 1
        elif picks[1] > 0:  # 철 곡괭이
            picks[1] -= 1
            for mineral in group:
                if mineral == 'diamond':
                    fatigue += 5
                else:
                    fatigue += 1
        elif picks[2] > 0:  # 돌 곡괭이
            picks[2] -= 1
            for mineral in group:
                if mineral == 'diamond':
                    fatigue += 25
                elif mineral == 'iron':
                    fatigue += 5
                else:
                    fatigue += 1

    return fatigue


# 테스트
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))  # 예상 출력: 12