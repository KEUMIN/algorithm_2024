def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    idx = 0
    for num in A:
        if B[idx] > num:
            answer += 1
            idx += 1

    return answer