def solution(commands):
    N = 50
    size = N * N

    def idx(r, c):
        return (int(r) - 1) * N + (int(c) - 1)

    parent = list(range(size))
    value = [""] * size  # 값은 루트에만 저장

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        # 병합된 값 규칙:
        # - 둘 다 값 있으면 a쪽(첫 번째 인자)의 값을 유지
        # - 하나만 있으면 그 값을 사용
        va, vb = value[ra], value[rb]
        parent[rb] = ra
        if va and not vb:
            pass  # a 값 유지
        elif not va and vb:
            value[ra] = vb
        # 둘 다 있을 때는 a 값 유지
        # 이전 rb는 루트가 아니므로 값은 비워도 되고 놔둬도 무관하지만 정리
        value[rb] = ""

    def update_cell(r, c, v):
        i = idx(r, c)
        root = find(i)
        value[root] = v

    def update_all(v1, v2):
        # 대표들만 바꾸면 충분하지만, 간단히 전 셀을 훑어도 2500이라 충분히 빠름
        for i in range(size):
            ri = find(i)
            if value[ri] == v1:
                value[ri] = v2

    def unmerge(r, c):
        i = idx(r, c)
        root = find(i)
        keep = value[root]  # 분해 전 값
        # 루트에 속한 모든 구성원을 찾아 단독 셀로 분리
        members = [j for j in range(size) if find(j) == root]
        for m in members:
            parent[m] = m
            value[m] = ""
        # 선택 셀만 기존 값을 유지
        value[i] = keep

    def print_cell(r, c):
        i = idx(r, c)
        v = value[find(i)]
        return v if v else "EMPTY"

    out = []
    for cmd in commands:
        parts = cmd.split()
        if parts[0] == "UPDATE":
            if len(parts) == 4:  # UPDATE r c value
                _, r, c, v = parts
                update_cell(r, c, v)
            else:  # UPDATE value1 value2
                _, v1, v2 = parts
                update_all(v1, v2)
        elif parts[0] == "MERGE":
            _, r1, c1, r2, c2 = parts
            a, b = idx(r1, c1), idx(r2, c2)
            if a != b:
                union(a, b)
        elif parts[0] == "UNMERGE":
            _, r, c = parts
            unmerge(r, c)
        elif parts[0] == "PRINT":
            _, r, c = parts
            out.append(print_cell(r, c))
    return out
