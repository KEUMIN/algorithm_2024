from collections import deque


def solution(n, t, m, timetable):
    timetable.sort()
    crew_idx = 0
    bus_time = convert_to_min("09:00")
    left_bus_cnt = n
    left_seats = m
    last_crew = convert_to_time(convert_to_min("09:00") + (n - 1) * t)

    while crew_idx < len(timetable) and left_bus_cnt > 0:
        if left_bus_cnt > 0:
            if left_seats == 0:
                bus_time += 10
                left_seats = m
                left_bus_cnt -= 1
        else:
            last_crew = timetable[crew_idx]

        crew = timetable[crew_idx]
        crew_t = convert_to_min(crew)

        if crew_t <= bus_time:
            crew_idx += 1
            left_seats -= 1

        else:
            if left_bus_cnt > 0:
                bus_time += 10
                left_seats = m
                left_bus_cnt -= 1

    if left_bus_cnt == 1:
        if left_seats == 0:
            last_crew = timetable[crew_idx - 1]
        elif left_seats > 0:
            print()
    elif left_bus_cnt > 1:
        print()

    return (
        convert_to_time(convert_to_min(last_crew) - 1)
        if left_seats == 0
        else convert_to_time(convert_to_min(last_crew))
    )


def convert_to_min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def convert_to_time(min):
    h, m = min // 60, min % 60
    return (
        (str(h) if h >= 10 else "0" + str(h))
        + ":"
        + (str(m) if m >= 10 else "0" + str(m))
    )


print(
    solution(
        10,
        60,
        45,
        [
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
        ],
    )
)
