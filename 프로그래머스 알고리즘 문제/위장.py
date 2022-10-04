from collections import defaultdict


def solution(clothes):
    d = defaultdict(int)
    for n, t in clothes:
        d[t] += 1

    answer = 1
    for i in d.values():
        answer *= (i + 1)
    return answer - 1