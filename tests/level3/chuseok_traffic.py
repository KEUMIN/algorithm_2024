# 프로그래머스 - 추석 트래픽 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/17676
# 사용 알고리즘 : 브루트 포스...

from datetime import datetime, timedelta


def solution(lines):
    cur_end = datetime.now()
    alpha = []
    max_cnt = -1

    for i, line in enumerate(lines):
        date, end, time = line.split()
        end = datetime.strptime(end, "%H:%M:%S.%f")
        time = str(float(time[:-1]))
        time = datetime.strptime(time, "%S.%f")
        start = end - time + datetime.strptime("0.001", "%S.%f")

        if i == 0 or start >= cur_end:
            cur_end = end + timedelta(seconds=1)
            alpha.append(end)
            for et in alpha:
                if et <= start:
                    alpha.remove(et)
            max_cnt = max(max_cnt, len(alpha))
        else:
            alpha.append(end)
            max_cnt = max(max_cnt, len(alpha))

    return max_cnt


print(
    solution(
        [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s",
        ]
    )
)
