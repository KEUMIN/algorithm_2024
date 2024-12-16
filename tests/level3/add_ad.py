def solution(play_time, adv_time, logs):
    def to_seconds(t):  # 시간을 초로 변환
        h, m, s = map(int, t.split(":"))
        return h * 3600 + m * 60 + s

    def to_hhmmss(t):  # 초를 HH:MM:SS로 변환
        h, m, s = t // 3600, (t % 3600) // 60, t % 60
        return f"{h:02}:{m:02}:{s:02}"

    play_time = to_seconds(play_time)
    adv_time = to_seconds(adv_time)
    timeline = [0] * (play_time + 1)

    # 로그로 타임라인 생성
    for log in logs:
        start, end = map(to_seconds, log.split("-"))
        timeline[start] += 1
        timeline[end] -= 1

    # 누적 재생 시간 계산
    for i in range(1, play_time + 1):
        timeline[i] += timeline[i - 1]
    for i in range(1, play_time + 1):
        timeline[i] += timeline[i - 1]

    # 광고 삽입 구간의 최대 누적 재생 시간 계산
    max_time, max_start = 0, 0
    for start in range(play_time - adv_time + 1):
        end = start + adv_time
        curr_time = timeline[end - 1] - (timeline[start - 1] if start > 0 else 0)
        if curr_time > max_time:
            max_time, max_start = curr_time, start

    return to_hhmmss(max_start)
