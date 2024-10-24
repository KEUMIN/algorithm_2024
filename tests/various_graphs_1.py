# 프로그래머스 - 도넛과 막대 그래프 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 사용 알고리즘 :
# 인사이트: 내 풀이와 정답의 차이 = 마지막 생성 정점 포착 방식과 도넛 그래프 개수를 구하는 디테일 차이
from collections import defaultdict


def solution(edges):
    result = [0] * 4
    adj = defaultdict(list)
    for e in edges:
        from_n, to_n = e
        adj[from_n].append(to_n)

    start_n = max(adj.items(), key=lambda x: len(x[1]))[0]
    result[0] = start_n

    def analyze(node):
        start_node = node
        cur_node = node
        while True:
            if cur_node not in adj:
                return "S"
            cur_list = adj[cur_node]
            if len(cur_list) == 2:
                return "E"
            tmp_node = cur_list[0]
            if tmp_node == start_node:
                return "D"
            cur_node = tmp_node

    for n in adj[start_n]:
        graph_type = analyze(n)
        if graph_type == "D":
            result[1] += 1
        elif graph_type == "S":
            result[2] += 1
        elif graph_type == "E":
            result[3] += 1

    return result


def answer(edges):
    result = [0] * 4
    adj = {}
    for e in edges:
        from_node, to_node = e
        if from_node not in adj:
            adj[from_node] = [0, 0]
        if to_node not in adj:
            adj[to_node] = [0, 0]
        adj[from_node][1] += 1
        adj[to_node][0] += 1

    for k, v in adj.items():
        if v[1] >= 2:
            if v[0] == 0:
                result[0] = k
            else:
                result[3] += 1
        elif v[1] == 0 and v[0] > 0:
            result[2] += 1

    result[1] = adj[result[0]][1] - (result[2] + result[3])

    return result
