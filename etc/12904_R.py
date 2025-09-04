# 중심 확장(Expand Around Center)


def solution(s: str) -> int:
    n = len(s)

    def expand(l: int, r: int) -> int:
        # s[l..r]를 중심으로 가능한 만큼 팰린드롬을 확장한 뒤 길이 반환
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1  # 마지막으로 한 번 넘친 뒤의 실제 길이

    best = 1
    for i in range(n - 1):
        best = max(
            best, expand(i, i), expand(i, i + 1)  # 홀수 길이 중심
        )  # 짝수 길이 중심
    return best
