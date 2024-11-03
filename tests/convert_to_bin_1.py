# 프로그래머스 - 이진 변환 반복하기 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s: str):
    result = [0, 0]
    num = s
    while num != "1":
        result[0] += 1
        ones = num.count("1")
        result[1] += len(num) - ones
        num = bin(ones)[2:]
    return result
