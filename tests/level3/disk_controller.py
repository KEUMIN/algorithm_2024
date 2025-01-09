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


import heapq


def answer_solution(jobs):
    # 요청 시간 기준으로 정렬
    jobs.sort(key=lambda x: x[0])

    current_time = 0
    total_turnaround_time = 0
    wait_queue = []
    job_index = 0
    job_count = len(jobs)

    while job_index < job_count or wait_queue:
        # 현재 시간까지 도달한 요청 작업들을 대기 큐에 추가
        while job_index < job_count and jobs[job_index][0] <= current_time:
            request_time, duration = jobs[job_index]
            heapq.heappush(wait_queue, (duration, request_time))
            job_index += 1

        if wait_queue:
            # 대기 큐에서 가장 소요 시간이 짧은 작업을 꺼냄
            duration, request_time = heapq.heappop(wait_queue)
            current_time += duration
            total_turnaround_time += current_time - request_time
        else:
            # 대기 큐가 비어 있는 경우, 시간을 진행
            current_time = jobs[job_index][0]

    return total_turnaround_time // job_count


print(solution([[0, 3], [1, 9], [3, 5]]))
