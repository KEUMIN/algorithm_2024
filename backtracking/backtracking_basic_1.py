# 백 트래킹 기본 문제 복습 1 - 주어진 숫자의 배열로 가능한 모든 순열 반환
def permutation(nums):
    def backtrack(arr):
        # 0. 재귀
        # 1. 탈출 조건
        if len(arr) == len(nums):
            result.append(arr[:])
            return

        # 2. 순회
        for num in nums:
            # 3. 순회 내 조건
            if num not in arr:
                # 4. 넣고, 재귀, 다시 빼기
                arr.append(num)
                backtrack(arr)
                arr.pop()

    result = []
    backtrack(arr=[])
    return result
