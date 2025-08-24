from collections import defaultdict, deque

def solution(n, vertex):
    m = defaultdict(list)
    for v in vertex:
        m[v[0]].append(v[1])
        m[v[1]].append(v[0])

    max_distance = -1
    answer = 0

    visit = set()
    q = deque([(1, 0)])
    visit.add(1)

    while q:
        cur_n, cur_d = q.popleft()
        if cur_d > max_distance:
            max_distance = cur_d
            answer = 1
        elif cur_d == max_distance:
            answer += 1

        for neighbor in m[cur_n]:
            if neighbor not in visit:
                q.append((neighbor, cur_d + 1))
                visit.add(neighbor)

    return answer