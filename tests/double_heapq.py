# 프로그래머스 - 이중 우선순위 큐 : https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 사용 알고리즘 : 우선순위 큐
import heapq


def solution(operations):
    values = []

    def pop_min():
        nonlocal values
        heapq.heapify(values)
        return heapq.heappop(values)

    def pop_max():
        nonlocal values
        values = [-v for v in values]
        heapq.heapify(values)
        maximum = -heapq.heappop(values)
        values = [-v for v in values]
        return maximum

    for op in operations:
        code, num = op.split()
        if code == "I":
            values.append(int(num))
        elif code == "D":
            if len(values) == 0:
                continue
            if num == "1":
                pop_max()
            else:
                pop_min()

    return (
        [0, 0]
        if len(values) == 0
        else [values[0], values[0]] if len(values) == 1 else [pop_max(), pop_min()]
    )


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
