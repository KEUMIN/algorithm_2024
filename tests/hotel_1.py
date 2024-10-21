# 프로그래머스 - 혼자 놀기의 달인 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/155651
# 사용 알고리즘 : 첫번째 내 풀이 - 그리디, 두번째 풀이 시작, 종료를 다른 이벤트로 나누는 이벤트 시뮬레이션, 스위핑


def solution(book_time):
    rooms = []
    book_time.sort(key=lambda x: (int(x[0][:2]), int(x[0][3:])))

    def validate_time(start, end):
        for i, cur_time in enumerate(rooms):
            cur_start, cur_end = cur_time
            if cur_end <= start:
                rooms[i] = (cur_start, end)
                return
        rooms.append((start, end))

    for t in book_time:
        start = (int(t[0][:2]) * 60) + int(t[0][3:])
        end = (int(t[1][:2]) * 60) + int(t[1][3:]) + 10
        if len(rooms) == 0:
            rooms.append((start, end))
            continue

        validate_time(start, end)

    return len(rooms)


def original_solution(book_time):
    events = []

    for start, end in book_time:
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))

        start_time = start_hour * 60 + start_minute
        end_time = end_hour * 60 + end_minute + 10

        events.append((start_time, "start"))
        events.append((end_time, "end"))

    events.sort(key=lambda x: (x[0], x[1] == "start"))

    current_rooms = 0
    max_rooms = 0

    for event in events:
        if event[1] == "start":
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
        else:
            current_rooms -= 1

    return max_rooms
