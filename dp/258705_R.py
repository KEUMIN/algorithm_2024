def solution(n, tops):
    MOD = 10007

    # i=0 초기값
    case0to2 = 3 if tops[0] == 1 else 2  # 깔끔 종료
    case3 = 1  # 걸쳐 남김

    # i=1..n-1
    for i in range(1, n):
        if tops[i] == 1:
            new_case0to2 = (case0to2 * 3 + case3 * 2) % MOD
        else:
            new_case0to2 = (case0to2 * 2 + case3 * 1) % MOD
        new_case3 = (case0to2 + case3) % MOD

        case0to2, case3 = new_case0to2, new_case3

    return (case0to2 + case3) % MOD