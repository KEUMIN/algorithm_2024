import heapq


def solution(jobs):
    N = len(jobs)
    queue = []
    time = 0
    tasks = []

    sorted_jobs = sorted(
        [(i, s, l) for i, (s, l) in enumerate(jobs)], key=lambda x: x[1], reverse=True
    )

    while len(tasks) < N:
        while sorted_jobs and time >= sorted_jobs[-1][1]:
            i, s, l = sorted_jobs.pop()
            heapq.heappush(queue, (l, s, i))

        if queue:
            l, s, i = heapq.heappop(queue)
            tasks.append((time + l) - s)
            time += l
        else:
            time = sorted_jobs[-1][1]

    return sum(tasks) // N
