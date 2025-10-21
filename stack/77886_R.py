def solution(strings):
    def make_lexicographically_smallest(s: str) -> str:
        stack = []
        count_110 = 0

        # 1) s에서 "110"을 모두 뽑아 개수 세기
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ["1", "1", "0"]:
                del stack[-3:]
                count_110 += 1

        remaining = "".join(stack)  # "110"을 제거하고 남은 문자열
        insert_after = remaining.rfind("0")  # 가장 오른쪽 '0'의 위치
        bundle_110 = "110" * count_110  # 한 번에 삽입할 "110" 묶음

        # 2) 사전순 최소가 되도록 삽입
        if insert_after == -1:  # '0'이 없으면 맨 앞에
            return bundle_110 + remaining
        return (
            remaining[: insert_after + 1] + bundle_110 + remaining[insert_after + 1 :]
        )

    return [make_lexicographically_smallest(s) for s in strings]
