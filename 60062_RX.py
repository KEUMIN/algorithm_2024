from itertools import permutations


def solution(n, weak, dist):
    L = len(weak)
    # 원형 → 선형으로 펼치기
    ext = weak + [w + n for w in weak]

    answer = float("inf")

    # 시작 인덱스를 weak의 각 위치로
    for start in range(L):
        segment = ext[start : start + L]

        # 투입 친구 수를 1명부터 증가
        for k in range(1, len(dist) + 1):
            # k명 뽑아 순서(방향)대로 배치 (시계/반시계는 "시작점 회전" + "친구 순열"로 커버)
            for friends in permutations(dist, k):
                used = 1  # 현재 사용하는 친구 수
                # 첫 친구가 덮을 수 있는 한계
                limit = segment[0] + friends[0]

                # 모든 취약 지점을 왼쪽→오른쪽으로 커버 가능한지 확인
                for pos in segment:
                    if pos > limit:
                        used += 1
                        if used > k:
                            break
                        limit = pos + friends[used - 1]
                else:
                    # 모두 커버 성공
                    answer = min(answer, k)
                    # 이 시작점에 대해 k명이면 더 적은 수는 이미 앞에서 시도했으므로 탈출
                    break

            # 이미 k명으로 성공했다면 다음 시작점으로
            if answer == k:
                break

    return -1 if answer == float("inf") else answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
