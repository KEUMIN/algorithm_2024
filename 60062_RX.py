from itertools import permutations


def solution(n, weak, dist):
    L = len(weak)
    # 원형을 일자로 펴기: weak[i] 뒤에 weak[i]+n을 이어붙임
    linear = weak + [w + n for w in weak]

    # 최소 투입 인원 탐색: 1명 ~ 모든 친구
    for k in range(1, len(dist) + 1):
        # 친구 k명을 어떤 순서로 투입할지 모든 순열 시도
        for friends in permutations(dist, k):
            # 시작점(취약 지점) L개 모두 시도
            for start in range(L):
                cnt = 1  # 현재 사용 중인 친구 수 (friends[cnt-1] 사용 중)
                reach = (
                    linear[start] + friends[cnt - 1]
                )  # 이 친구가 커버 가능한 최우측 지점
                ok = True

                # start부터 start+L-1까지 L개의 취약지점을 모두 커버 가능한지 체크
                for idx in range(start, start + L):
                    if linear[idx] > reach:  # 현재 친구로 못 덮으면 다음 친구 투입
                        cnt += 1
                        if cnt > k:  # 준비한 k명을 초과하면 실패
                            ok = False
                            break
                        reach = (
                            linear[idx] + friends[cnt - 1]
                        )  # 새 친구의 도달 한계 갱신

                if ok:
                    return k

    # 어떤 경우로도 덮지 못함
    return -1


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
