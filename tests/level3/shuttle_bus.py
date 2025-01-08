from collections import deque


def solution(n, t, m, timetable):
    queue = deque(sorted(timetable))
    bus_time = convert_to_min("09:00")
    max_time = 0
    last_passenger = ""

    for i in range(n):
        passengers = m
        while m:
            if not queue:
                max_time = bus_time
                break
            cur_p = queue.popleft()
            cur_p_time = convert_to_min(cur_p)
            if bus_time >= cur_p_time:
                passengers -= 1
                if i == n - 1 and passengers == 1:
                    last_passenger = cur_p
            else:
                queue.appendleft(cur_p)
                break
        bus_time += t

    print(convert_to_time(max_time))
    print(last_passenger)
    return


def convert_to_min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def convert_to_time(min):
    h, m = min // 60, min % 60
    return str(h) if h >= 10 else "0" + str(h) + ":" + str(m)


solution(2, 10, 2, ["09:10", "09:09", "08:00"])
