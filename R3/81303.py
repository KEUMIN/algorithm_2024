def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    linked_list[0][0], linked_list[n - 1][1] = -1, -1

    del_stack = []
    removed = ["O"] * n
    curr = k

    for c in cmd:
        if c == "C":
            removed[curr] = "X"
            prev, nxt = linked_list[curr]
            del_stack.append((prev, curr, nxt))

            if prev != -1:
                linked_list[prev][1] = nxt
            if nxt != -1:
                linked_list[nxt][0] = prev

            if nxt != -1:
                curr = nxt
            else:
                curr = prev

        elif c == "Z":
            prev, now, nxt = del_stack.pop()
            removed[now] = "O"

            if prev != -1:
                linked_list[prev][1] = now
            if nxt != -1:
                linked_list[nxt][0] = now

        else:
            direction, dist = c.split()
            for _ in range(int(dist)):
                curr = (
                    linked_list[curr][0] if direction == "U" else linked_list[curr][1]
                )

    return "".join(removed)


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
