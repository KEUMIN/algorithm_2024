# 프로그래머스 - 추석 트래픽 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/17676
# 사용 알고리즘 : 브루트 포스
# 인사이트 : 끝 구간 + 1초 아이디어는 맞았으나, 구간의 시작과 끝 모두 1초 구간을 구하고 N번 다시 순회할거라는 생각은 못했다...

from datetime import datetime, timedelta


def solution(lines):
    # 시작시간과 종료시간을 저장
    times = []
    for line in lines:
        date, end_time, duration = line.split()
        end = datetime.strptime(end_time, "%H:%M:%S.%f")
        duration = float(duration[:-1])
        start = end - timedelta(seconds=duration) + timedelta(milliseconds=1)
        times.append((start, end))

    max_traffic = 0
    # 각 로그의 시작과 끝 시점에서 1초 구간 체크
    for i in range(len(times)):
        for check_time in (times[i][0], times[i][1]):
            count = 0
            check_end = check_time + timedelta(seconds=1)
            for start, end in times:
                if start < check_end and end >= check_time:
                    count += 1
            max_traffic = max(max_traffic, count)

    return max_traffic
