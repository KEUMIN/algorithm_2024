# 프로그래머스 - 영어 끝말잇기 (LV2) : https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 사용 알고리즘 : 해시
# 풀이: 문제 상 주체와 객체를 바꿔서 생각한다. (주체: 플레이어 <-> 객체: 단어)
from collections import defaultdict


def solution(n, words):
    word_dict = defaultdict(int)
    former = words[0][-1]
    word_dict[words[0]] += 1
    for i in range(1, len(words)):
        if former == words[i][0] and words[i] not in word_dict:
            former = words[i][-1]
            word_dict[words[i]] += 1
        else:
            return [i % n + 1, i // n + 1]
    return [0, 0]
