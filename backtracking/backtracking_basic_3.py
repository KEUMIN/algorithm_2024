# 주어진 숫자 리스트 nums에서 합이 target인 K개의 조합이 있을 경우 참을 반환


def solution(nums: list[int], k: int, target: int) -> bool:
    def backtrack(start: int, arr: list[int]):
        result = False

        if len(arr) == k:
            if sum(arr) == target:
                return True
            else:
                return False

        for i in range(start, len(nums)):
            arr.append(nums[i])
            result = backtrack(i + 1, arr)
            if result:
                return True
            arr.pop()

        return result

    result = backtrack(0, [])
    return result
