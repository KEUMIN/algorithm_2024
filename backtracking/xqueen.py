def solution(n):
    def is_safe(queens, row, col):
        # 현재 열과 대각선에 이미 퀸이 있는지 확인
        for r in range(row):
            if queens[r] == col or \
               queens[r] - r == col - row or \
               queens[r] + r == col + row:
                return False
        return True

    def place_queens(row, queens):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                count += place_queens(row + 1, queens)
        return count
    
    # 각 행의 퀸의 위치를 저장할 배열
    queens = [-1] * n
    return place_queens(0, queens)

# 테스트 예제
print(solution(4))  # 출력: 2
print(solution(8))  # 출력: 92
