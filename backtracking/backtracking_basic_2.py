# [1,2,3,4] 주어진 수로 K개 조합 찾기


def solution(nums: list[int], k: int):
    result: list[list[int]] = []

    def backtrack(start: int, arr: list[int]):
        if len(arr) == k and arr not in result:
            result.append(arr[:])
            return

        for i in range(start, len(nums)):
            arr.append(nums[i])
            backtrack(i + 1, arr)
            arr.pop()

    backtrack(start=0, arr=[])
    return result


# 결과적으로 from itertools import combinations와 같음
