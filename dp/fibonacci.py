#12945

def solution(n):
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2]) % 1234567
    return lst[n]