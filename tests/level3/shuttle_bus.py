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


def answer_solution(n, t, m, timetable):
    # 시간을 분으로 변환 후 정렬
    crew_times = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timetable)
    shuttle_time = 540  # 첫 셔틀 시간 (09:00)

    for _ in range(n):
        # 현재 셔틀에 태울 수 있는 크루들
        available_crews = [time for time in crew_times if time <= shuttle_time]

        if len(available_crews) > m:  # 정원이 넘치면
            crew_times = crew_times[m:]  # m명만 태우고 나머지 유지
        else:  # 정원이 안 넘치면
            crew_times = crew_times[len(available_crews) :]

        # 마지막 셔틀이면 조건 확인
        if _ == n - 1:
            if len(available_crews) >= m:
                # 마지막 셔틀이 꽉 찬 경우, 마지막 태운 사람보다 1분 빠르게 도착
                return f"{(available_crews[m - 1] - 1) // 60:02}:{(available_crews[m - 1] - 1) % 60:02}"
            else:
                # 정원이 남는 경우, 셔틀 시간에 도착
                return f"{shuttle_time // 60:02}:{shuttle_time % 60:02}"

        # 다음 셔틀 시간 갱신
        shuttle_time += t
