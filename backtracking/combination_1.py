# 1부터 N까지 수 중 합이 10인 조합을 출력


def solution(N: int) -> list[list[int]]:
    result = []

    def backtrack(sum: int, arr: list[int], start: int):
        if sum == 10:
            result.append(arr[:])
            return
        elif sum > 10:
            return

        for i in range(start, N + 1):
            arr.append(i)
            backtrack(sum + i, arr, i + 1)
            arr.pop()

    backtrack(sum=0, arr=[], start=1)
    return result
