# 프로그래머스 - 야근 지수 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/12927
# 사용 알고리즘 : 우선순위 큐
# 문제 키워드 : 우선순위 큐(heapq)를 사용하는 문제는 가장 작은/큰 요소를 반복적으로 다룰 때 사용된다. heappop은 가장 작은 걸 반환.
# 문제 예시 : K번째로 큰 수 찾기...
import heapq


def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)

    for i in range(n):
        max_work = heapq.heappop(works)
        if max_work == 0:
            break
        heapq.heappush(works, max_work + 1)

    return sum([work * work for work in works])
