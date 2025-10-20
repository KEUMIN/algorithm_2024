def solution(n, build_frame):
    structure_set = set()

    def convert(x, y, a):
        return str(x) + " " + str(y) + " " + str(a)

    def can_build(x, y, a, b):
        if a == 0:
            if (
                y == 0
                or (
                    convert(x - 1, y, 1) in structure_set
                    or convert(x, y, 1) in structure_set
                )
                or convert(x, y - 1, 0) in structure_set
            ):
                return True
            else:
                return False
        else:
            if (
                convert(x, y - 1, 0) in structure_set
                or convert(x + 1, y - 1, 0) in structure_set
            ) or (
                convert(x - 1, y, 1) in structure_set
                and convert(x + 1, y, 1) in structure_set
            ):
                return True
            else:
                return False

    for x, y, a, b in build_frame:
        if can_build(x, y, a, b):
            if b == 1:
                structure_set.add(convert(x, y, a))
            else:
                structure_set.remove(convert(x, y, a))

    return sorted([[int(c) for c in s.split()] for s in structure_set])


print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)
