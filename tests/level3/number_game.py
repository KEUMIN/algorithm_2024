# 프로그래머스 - 숫자 게임 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/12987
# 사용 알고리즘 : 그리디
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    idx = 0
    for num in A:
        if idx >= len(B):
            break
        if B[idx] > num:
            answer += 1
            idx += 1

    return answer


solution([5, 1, 3, 7], [2, 2, 6, 8])
