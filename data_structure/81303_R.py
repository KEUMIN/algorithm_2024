# 시간 복잡도 초과....


def solution(n, k, cmd):
    arr = [True] * n
    lst = [i for i in range(n)]
    d_stack = []
    cur_i = k

    for c in cmd:
        if c.startswith("D"):
            cur_i += int(c.split()[1])
        elif c.startswith("U"):
            cur_i -= int(c.split()[1])
        elif c.startswith("C"):
            d_stack.append((cur_i, lst[cur_i]))
            if cur_i == len(lst) - 1:
                lst = lst[:cur_i]
                cur_i -= 1
            else:
                lst = lst[:cur_i] + lst[cur_i + 1 :]
        else:
            latest_d_i, value = d_stack.pop()
            lst = lst[:latest_d_i] + [value] + lst[latest_d_i:]
            cur_i = cur_i + 1 if latest_d_i <= cur_i else cur_i

    while d_stack:
        _, idx = d_stack.pop()
        arr[idx] = False

    answer = ""
    for b in arr:
        answer += "O" if b else "X"
    return answer
