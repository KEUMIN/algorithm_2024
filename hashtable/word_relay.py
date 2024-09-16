#12981
from collections import defaultdict

def solution(n, words):
    word_dict = defaultdict(int)
    start_char = words[0][0]

    for i, word in enumerate(words):
        if word_dict[word] > 0 or start_char != word[0]:
            return [(i%n) + 1, (i//n) + 1]
        else:
            word_dict[word] += 1
            start_char = word[len(word) - 1]

    return [0,0]
