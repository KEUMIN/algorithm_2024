# 프로그래머스 - 과제 진행하기 : https://school.programmers.co.kr/learn/courses/30/lessons/176962
# 사용 알고리즘 : 브루트 포스???
def solution(plans):
    convert_plan_times(plans)
    plans.sort(key=lambda x: x[1])
    answer = []
    stack = []
    for i in range(0, len(plans) - 1):
        c_name, c_start, c_time = plans[i]
        n_name, n_start, n_time = plans[i + 1]
        if c_start + c_time > n_start:
            stack.append((c_name, c_start + c_time - n_start))
        else:
            answer.append(c_name)
            left_t = n_start - (c_start + c_time)
            process_left(left_t, stack, answer)

    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    print(answer)
    return answer


def process_left(time, queue, answer):
    left_t = time
    while queue and left_t > 0:
        w_n, w_t = queue.pop()
        if left_t >= w_t:
            left_t -= w_t
            answer.append(w_n)
        else:
            queue.append((w_n, w_t - left_t))
            left_t = 0


def convert_plan_times(plans):
    for plan in plans:
        plan[1] = str_to_num(plan[1])
        plan[2] = int(plan[2])


def str_to_num(time):
    h, m = time.split(":")
    return (int(h) * 60) + int(m)
