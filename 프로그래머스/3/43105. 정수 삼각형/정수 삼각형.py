def solution(triangle):
    # 삼각형을 아래에서부터 위로 올라가며 합을 계산
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            
            # 현재 위치의 값에 아래 행의 두 대각선 값 중 더 큰 값을 더함
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
            
    # 최종적으로 꼭대기 값에 최대 합이 저장됨
    return triangle[0][0]