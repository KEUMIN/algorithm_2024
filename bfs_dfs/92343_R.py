from collections import deque

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)

    max_sheep = 0
    queue = deque([(0, 1, 0, set())])

    while queue:
        node, sheep, wolves, visit = queue.popleft()
        max_sheep = max(max_sheep, sheep)
        visit.update(tree[node])
        for n in visit:
            if info[n]:
                if sheep > wolves + 1:
                    queue.append((n, sheep, wolves + 1, visit - {n}))
            else:
                    queue.append((n, sheep + 1, wolves, visit - {n}))

    return max_sheep