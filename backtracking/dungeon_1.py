# 프로그래머스 - 피로도 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/87946


def solution(k, dungeons):
    return backtrack(
        cur_fatigue=k, count=0, visit=[False] * len(dungeons), dungeons=dungeons
    )


def backtrack(cur_fatigue, count, visit, dungeons):
    result = count

    for idx, d in enumerate(dungeons):
        if cur_fatigue >= d[0] and not visit[idx]:
            visit[idx] = True
            result = max(
                backtrack(cur_fatigue - d[1], count + 1, visit, dungeons), result
            )
            visit[idx] = False

    return result


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
