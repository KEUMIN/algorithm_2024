# 프로그래머스 - 인사고과 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/152995
# 사용 알고리즘 : 정렬, 필터링, 시뮬레이션


def solution(scores):
    for i in range(1, len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return -1

    final_lst = filter_scores(scores)
    final_lst.sort(key=lambda x: x[2] == "w", reverse=True)

    w_rank = 1
    for i in range(1, len(final_lst)):
        if final_lst[i][0] + final_lst[i][1] > final_lst[0][0] + final_lst[0][1]:
            w_rank += 1

    return w_rank


def filter_scores(scores):
    scores = [score + ["o"] for score in scores]
    scores[0][2] = "w"
    a_sort = sorted(scores, key=lambda x: (x[0], x[1]), reverse=True)
    filtered = set()

    max_b = a_sort[0][1]
    tmp_a = a_sort[0][0]
    tmp_b = a_sort[0][1]

    for i in range(1, len(a_sort)):
        if a_sort[i][0] == a_sort[0][0]:
            continue

        if a_sort[i][1] < max_b:
            filtered.add(i)

        if a_sort[i][0] < tmp_a:
            tmp_a = a_sort[i][0]
            max_b = max(max_b, tmp_b)
        tmp_b = max(tmp_b, a_sort[i][1])

    return [a_sort[i] for i, score in enumerate(a_sort) if i not in filtered]


# 정답 풀이
def answer_solution(scores):
    # 완호의 점수
    wanho = scores[0]

    # 근무 태도 점수를 내림차순, 같으면 동료 평가 점수를 오름차순으로 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))

    max_peer_score = 0
    incentive_candidates = []

    # 점수 필터링
    for attitude, peer in scores:
        if peer < max_peer_score:
            if [attitude, peer] == wanho:
                return -1  # 완호가 탈락
        else:
            max_peer_score = peer
            incentive_candidates.append((attitude, peer))

    # 최종 석차 계산
    incentive_candidates.sort(key=lambda x: -(x[0] + x[1]))
    rank = 1
    prev_sum = -1
    skip_rank = 0

    for attitude, peer in incentive_candidates:
        score_sum = attitude + peer
        if score_sum != prev_sum:
            rank += skip_rank
            skip_rank = 0
            prev_sum = score_sum
        if [attitude, peer] == wanho:
            return rank
        skip_rank += 1
