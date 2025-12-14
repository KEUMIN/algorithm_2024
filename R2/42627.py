import heapq


def solution(jobs):
    # jobs[i] = [요청시각 s, 소요시간 l]
    # 우선순위: 소요시간 짧은 것 → 요청시각 빠른 것 → 작업번호 작은 것
    n = len(jobs)
    # (요청시각, 소요시간, 작업번호)로 정규화 후 요청시각 기준 정렬
    arr = sorted([(s, l, i) for i, (s, l) in enumerate(jobs)], key=lambda x: x[0])

    pq = []  # (소요시간, 요청시각, 작업번호)
    time = 0
    idx = 0
    done = 0
    total_turnaround = 0

    while done < n:
        # 현재 시각까지 도착한 작업을 모두 PQ에 넣기
        while idx < n and arr[idx][0] <= time:
            s, l, i = arr[idx]
            heapq.heappush(pq, (l, s, i))
            idx += 1

        if pq:
            l, s, i = heapq.heappop(pq)
            time += l  # 작업 수행
            total_turnaround += time - s  # (종료시각 - 요청시각)
            done += 1
        else:
            # 대기 큐가 비었으면, 다음 작업의 도착 시각으로 점프
            # (디스크가 노는 시간을 불필요하게 1ms씩 흘리지 않기)
            time = arr[idx][0]

    return total_turnaround // n
