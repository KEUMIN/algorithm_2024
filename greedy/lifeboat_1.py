# 프로그래머스 - 구명보트 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 사용 알고리즘 : 그리디, 투포인터


def solution(people, limit):
    sorted_people = sorted(people)
    i = 0
    j = len(people) - 1
    count = 0
    while i <= j:
        if sorted_people[i] + sorted_people[j] <= limit:
            i += 1
        j -= 1
        count += 1

    return count
