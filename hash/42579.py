import heapq
from collections import defaultdict


def solution(genres, plays):
    genres_tot = defaultdict(int)
    plays_rank = defaultdict(list)

    for i in range(len(genres)):
        genres_tot[genres[i]] += plays[i]
        heapq.heappush(plays_rank[genres[i]], (plays[i] * -1, i))

    result = []
    for g, _ in sorted(genres_tot.items(), key= lambda x: x[1], reverse=True):
        for _ in range(2):
            if plays_rank[g] : result.append(heapq.heappop(plays_rank[g])[1])

    return result