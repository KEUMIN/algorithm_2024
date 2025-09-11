def solution(scores):
    w_a = scores[0][0]
    w_p = scores[0][1]

    scores.sort(key=lambda x: (-x[0], x[1]))

    sum_list = []
    max_p = scores[0][1]

    for a, p in scores:
        if p < max_p:
            if a == w_a and p == w_p:
                return -1
        else:
            max_p = max(max_p, p)
            sum_list.append(a + p)

    for i, s in enumerate(sorted(sum_list, reverse=True)):
        if s == w_a + w_p:
            return i + 1
