def solution(a):
    min_vals = set()
    left_min = float('INF')
    right_min = float('INF')
    for i in range(len(a)):
        if a[i] < left_min:
            min_vals.add(a[i])
            left_min = a[i]

    for j in range(len(a) - 1, -1, -1):
        if a[j] < right_min:
            min_vals.add(a[j])
            right_min = a[j]

    return len(min_vals)