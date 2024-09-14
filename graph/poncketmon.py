#1845 매우 쉬움
from collections import Counter

def solution(nums):
    cnt = Counter(nums)
    if len(nums) / 2 >= len(cnt.keys()):
        return len(cnt.keys())
    else:
        return len(nums) / 2