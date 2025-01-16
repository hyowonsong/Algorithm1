def solution(board, skill):
    n, m = len(board), len(board[0])
    # 차이 배열 초기화
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    # 스킬 정보 적용
    for type_, r1, c1, r2, c2, degree in skill:
        value = degree if type_ == 2 else -degree
        diff[r1][c1] += value
        diff[r1][c2 + 1] -= value
        diff[r2 + 1][c1] -= value
        diff[r2 + 1][c2 + 1] += value

    # 행 방향 누적 합
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j - 1]

    # 열 방향 누적 합
    for j in range(m):
        for i in range(1, n):
            diff[i][j] += diff[i - 1][j]

    # 최종 내구도 계산 및 파괴되지 않은 건물 카운트
    count = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                count += 1

    return count