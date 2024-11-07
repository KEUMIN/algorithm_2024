# 프로그래머스 - 불량 사용자 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/64064
# 사용 알고리즘 : 해시 & 조합(경우의 수)
# 문제 키워드 : frozenset은 불변이기 때문에 키 값으로 해싱이 가능하여 map이나 set에 넣을 수 있다.


def solution(user_id, banned_id):
    def fit_in(ban_id, user_id):
        if len(ban_id) != len(user_id):
            return False
        for b, u in zip(ban_id, user_id):
            if b != "*" and b != u:
                return False
        return True

    result_set = set()

    def dfs(start, path):
        if start == len(banned_id):
            result_set.add(frozenset(path))
            return

        current_ban = banned_id[start]
        for user in user_id:
            if user not in path and fit_in(current_ban, user):
                dfs(start + 1, path + [user])

    dfs(0, [])
    return len(result_set)
