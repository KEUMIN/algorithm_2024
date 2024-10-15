# 프로그래머스 - 광물 캐기 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 문제 : 마인이 작업을 끝내기까지 필요한 최소한의 피로도를 구하시오.
# 사용 알고리즘 : 그리디


def solution(picks, minerals):
    num_of_picks = sum(picks)
    # 광물 리스트를 5개씩 묶어서 리스트의 리스트로 만듦
    mineral_groups = [minerals[i : i + 5] for i in range(0, len(minerals), 5)]
    # 가용 곡괭이 만큼 광물 그룹 리스트를 재단
    mineral_groups = mineral_groups[:num_of_picks]

    # 각 그룹의 가치 계산 (다이아몬드 곡괭이로 캘 때의 피로도)
    def group_value(group):
        value = 0
        for mineral in group:
            if mineral == "diamond":
                value += 25
            elif mineral == "iron":
                value += 5
            else:
                value += 1
        return value

    mineral_groups = sorted(mineral_groups, key=group_value, reverse=True)

    def consume_picks(sorted_minerals):
        tot_fatigue = 0
        for minerals in sorted_minerals:
            if picks[0] > 0:
                tot_fatigue += len(minerals)
                picks[0] -= 1
            elif picks[1] > 0:
                for mineral in minerals:
                    if mineral == "diamond":
                        tot_fatigue += 5
                    else:
                        tot_fatigue += 1
                picks[1] -= 1
            elif picks[2] > 0:
                for mineral in minerals:
                    if mineral == "diamond":
                        tot_fatigue += 25
                    elif mineral == "iron":
                        tot_fatigue += 5
                    else:
                        tot_fatigue += 1
                picks[2] -= 1

        return tot_fatigue

    return consume_picks(mineral_groups)
