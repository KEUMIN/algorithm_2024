# 프로그래머스 - 전화번호 목록 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 사용 알고리즘 : 해시


def solution(phone_book):
    phone_set = set()
    for num in sorted(phone_book, key=len):
        for i in range(len(num)):
            if num[: i + 1] in phone_set:
                return False
        phone_set.add(num)
    return True
