# 프로그래머스 - 억억단을 외우자 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/138475
# 사용 알고리즘 : 소수 구하기

from collections import defaultdict


# 내 풀이
def my_solution(e, starts):
    answer = []
    min_num = min(starts)

    def count(n):
        count = 0
        for i in range(1, int(n ** (0.5)) + 1):
            if n % i == 0:
                count += 1
                if n // i != i:
                    count += 1
        return count

    cnt_dict = defaultdict(int)
    for i in range(min_num, e + 1):
        cnt_dict[i] = count(i)

    def find_max(n):
        lst = sorted(
            [i for i in cnt_dict.items() if i[0] >= n], key=lambda x: (-x[1], x[0])
        )
        return lst[0][0]

    return [find_max(n) for n in starts]


def solution(e, starts):
    # 각 숫자의 약수의 개수를 계산 (등장 횟수와 동일)
    counts = [1] * (e + 1)  # 1은 모든 수의 약수

    # 에라토스테네스의 체와 비슷한 방식으로 약수 개수 계산
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            counts[j] += 1

    # 각 범위에서의 최댓값을 미리 계산
    max_counts = [0] * (e + 1)
    max_num = e
    curr_max_count = counts[e]

    # 뒤에서부터 순회하며 최댓값 갱신
    for i in range(e, 0, -1):
        if counts[i] >= curr_max_count:
            max_num = i
            curr_max_count = counts[i]
        max_counts[i] = max_num

    # 각 시작점에 대한 결과 반환
    return [max_counts[s] for s in starts]


print(solution(8, [1, 3, 7]))
