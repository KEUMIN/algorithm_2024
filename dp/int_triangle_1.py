# 프로그래머스 - 정수 삼각형 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 사용 알고리즘 : 동적 프로그래밍 [점화식]
# 풀이 : 힌트 (한 단계씩 더해가며 최종적으로 최대/최소값을 원할 경우) + 풀이 (동일한 0으로 채워진 자료구조를 하나 더 만들어서 단계적으로 접근)


def solution(triangle):
    sum_tri = [[0] * i for i in range(1, len(triangle) + 1)]
    sum_tri[0] = triangle[0]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            prev = (
                max(sum_tri[i - 1][j - 1 : j + 1])
                if (j - 1) >= 0 and j < len(triangle[i])
                else (sum_tri[i - 1][j] if (j - 1) < 0 else sum_tri[i - 1][j - 1])
            )
            sum_tri[i][j] = prev + triangle[i][j]

    return max(sum_tri[len(triangle) - 1])
