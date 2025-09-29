def solution(a):
    answer = 0
    less_exists_from_left = [False] * len(a)
    less_exists_from_right = [False] * len(a)

    left_min_val = a[0]

    for i in range(1, len(a)):
        if left_min_val > a[i]:
            left_min_val = a[i]
        else:
            less_exists_from_left[i] = True

    right_min_val = a[-1]

    for i in range(len(a) - 2, -1, -1):
        if right_min_val > a[i]:
            right_min_val = a[i]
        else:
            less_exists_from_right[i] = True

    for i in range(len(a)):
        if not less_exists_from_left[i] or not less_exists_from_right[i]:
            answer += 1

    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
