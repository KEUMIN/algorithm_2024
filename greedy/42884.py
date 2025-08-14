def solution(routes):
    s_route = sorted(routes)
    prev_start, prev_end = s_route[0]
    result = 1

    for i in range(1, len(s_route)):
        cur_start, cur_end = s_route[i]
        if prev_end < cur_start:
            prev_start, prev_end = cur_start, cur_end
            result += 1

        else:
            if cur_end < prev_end:
                prev_end = cur_end

    return result


# def solution(routes):
#     result = 1
#     routes.sort(key=lambda x: x[1])
#     cur_end = routes[0][1]
#
#     for i in range(1, len(routes)):
#         if routes[i][0] > cur_end:
#             cur_end = routes[i][1]
#             result += 1
#
#     return result
