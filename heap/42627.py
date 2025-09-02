import heapq

def solution(jobs):
    q = []
    for i, j in enumerate(jobs):
        heapq.heappush(q, (j[1], j[0], i))

    tot_dur = 0
    prev_task_t = 0
    while q:
        dur, req_time, _ = heapq.heappop(q)
        tot_dur += dur + (prev_task_t - req_time if prev_task_t - req_time > 0 else 0)
        prev_task_t = req_time + dur if req_time > prev_task_t else prev_task_t + dur

    return tot_dur // len(jobs)