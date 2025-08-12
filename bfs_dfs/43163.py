from collections import deque, defaultdict

def solution(begin, target, words):
    if target not in words:
        return 0

    visit = set()
    def bfs(first_word):
        visit.add(first_word)
        q = deque([(first_word, 0)])

        while q:
            cur_word, dist = q.popleft()
            if cur_word == target:
                return dist

            for w in words:
                if w not in visit and can_change(cur_word, w):
                    q.append((w, dist + 1))
                    visit.add(w)

    result = bfs(begin)
    return result



def can_change(source, target):
    diff_cnt = 0
    for i in range(len(source)):
        if source[i] != target[i]:
            diff_cnt += 1
    return True if diff_cnt == 1 else False

print(solution("hit", "cog", 	["hot", "dot", "dog", "lot", "log", "cog"]))
