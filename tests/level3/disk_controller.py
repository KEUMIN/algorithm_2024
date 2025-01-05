# 프로그래머스 - 디스크 컨트롤러 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 사용 알고리즘 : 힙
import heapq


def solution(jobs):
    n_jobs = []
    for i, job in enumerate(jobs):
        n_jobs.append(
            [(job[1] * 10000000 + (job[0] + 1) * 1000 + i), job[0], job[1], i]
        )
    heapq.heapify(n_jobs)
    job_sum = 0
    return_sum = 0
    while n_jobs:
        cur_job = heapq.heappop(n_jobs)
        request_time = cur_job[1]
        work_time = cur_job[2]
        job_sum += work_time
        return_sum += job_sum - request_time

    return return_sum // len(jobs)


print(solution([[0, 3], [1, 9], [3, 5]]))
