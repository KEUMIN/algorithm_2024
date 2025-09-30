import heapq


def solution(jobs):
    N = len(jobs)
    i_jobs = [[job[1], job[0], i] for i, job in enumerate(jobs)]
    heapq.heapify(i_jobs)
    s_t = 0
    tmp = []
    results = []
    while i_jobs or tmp:
        if not i_jobs:
            while tmp:
                heapq.heappush(i_jobs, tmp.pop())
            s_t += 1

        if i_jobs[0][1] <= s_t:
            l, s, _ = heapq.heappop(i_jobs)
            s_t += l
            results.append(s_t - s)
            while tmp:
                heapq.heappush(i_jobs, tmp.pop())
        else:
            tmp.append(heapq.heappop(i_jobs))

    return sum(results) // N
