import heapq


def solution(n, t, m, timetable):
    times = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in timetable]
    heapq.heapify(times)

    number_of_bus = n
    start = 540
    cur_bus_time = start
    cur_bus_capacity = m
    last_p_t = start

    while number_of_bus > 0:
        last_p_t = cur_bus_time
        cur_bus_capacity = m
        while times and cur_bus_capacity > 0:
            if times[0] > cur_bus_time:
                break
            passenger = heapq.heappop(times)
            if cur_bus_capacity == 1:
                last_p_t = passenger
            cur_bus_capacity -= 1

        if number_of_bus != 1:
            cur_bus_time += t
        number_of_bus -= 1

    return (
        convert_to_timestamp(cur_bus_time)
        if cur_bus_capacity > 0
        else convert_to_timestamp(last_p_t - 1)
    )


def convert_to_timestamp(x):
    return f"{x//60:02d}:{x%60:02d}"
