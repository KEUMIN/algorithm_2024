def solution(a):
    num_set = set()
    l_min = float("INF")
    r_min = float("INF")

    for i in range(len(a)):
        if l_min > a[i]:
            l_min = a[i]
            num_set.add(a[i])

    for j in range(len(a) - 1, -1, -1):
        if r_min > a[j]:
            r_min = a[j]
            num_set.add(a[j])

    return len(num_set)
