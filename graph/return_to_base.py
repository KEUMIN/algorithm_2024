#132266
#내 풀이 - 일반적인 인접리스트와 bfs로 접근 : 시간 복잡도에서 미 통과, 개선 필요
#수정 - 시작에서 종착지로 가는 편견, 종착지에 시작해서 각 -1인 거리를 개선해 나가는 접근
from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    adj = defaultdict(list)
    for con in roads:
        adj[con[0]].append(con[1])
        adj[con[1]].append(con[0])

    def bfs(adj, start, n):
        queue = deque([start])
        distances = [-1 for _ in range(n + 1)]
        distances[start] = 0

        while queue:
            current = queue.popleft()
            for neighbor in adj[current]:
                if distances[neighbor] == -1:
                    queue.append(neighbor)
                    distances[neighbor] = distances[current] + 1

        return distances

    distances = bfs(adj, destination, n)
    return [distances[source] for source in sources]

#print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
