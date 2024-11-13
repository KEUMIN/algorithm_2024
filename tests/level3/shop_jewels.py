# 프로그래머스 - 보석 쇼핑 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 사용 알고리즘 : 투 포인터
# 인사이트 : "모든 걸 포함하는 최소 구간"


def solution(gems):
    n = len(gems)
    gem_types = len(set(gems))  # 보석의 종류 수

    # 보석이 1종류면 첫 번째 위치만 반환
    if gem_types == 1:
        return [1, 1]

    # 현재 구간에 포함된 보석들을 저장할 딕셔너리
    gem_count = {}
    answer = [1, n]  # 초기값은 전체 구간

    start = 0
    end = 0

    while end < n:
        # end 포인터를 이동하면서 보석 추가
        if gems[end] not in gem_count:
            gem_count[gems[end]] = 1
        else:
            gem_count[gems[end]] += 1

        # 현재 구간에 모든 종류의 보석이 포함되었다면
        while len(gem_count) == gem_types:
            # 현재 구간이 기존 구간보다 짧거나,
            # 같은 길이지만 시작점이 더 작다면 정답 갱신
            if (end - start) < (answer[1] - answer[0]) or (
                (end - start) == (answer[1] - answer[0]) and start < answer[0]
            ):
                answer = [start + 1, end + 1]

            # start 포인터를 이동하면서 보석 제거
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]
            start += 1

        end += 1

    return answer
