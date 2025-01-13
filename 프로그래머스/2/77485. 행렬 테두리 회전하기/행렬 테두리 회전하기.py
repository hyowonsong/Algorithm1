def solution(rows, columns, queries):
    # 초기 행렬 생성
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = (i - 1) * columns + j
    
    result = []
    
    # 각 쿼리에 대해 회전 수행
    for x1, y1, x2, y2 in queries:
        min_value = float('inf')
        
        # 회전 전 첫 번째 요소 저장
        temp = matrix[x1][y1]
        
        # 왼쪽 세로 변 이동 (아래에서 위로)
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i + 1][y1]
            min_value = min(min_value, matrix[i][y1])
        
        # 아래쪽 가로 변 이동 (오른쪽에서 왼쪽으로)
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i + 1]
            min_value = min(min_value, matrix[x2][i])
        
        # 오른쪽 세로 변 이동 (위에서 아래로)
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i - 1][y2]
            min_value = min(min_value, matrix[i][y2])
        
        # 위쪽 가로 변 이동 (왼쪽에서 오른쪽으로)
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i - 1]
            min_value = min(min_value, matrix[x1][i])
        
        # 저장해둔 첫 번째 요소를 마지막 위치에 배치
        matrix[x1][y1 + 1] = temp
        min_value = min(min_value, temp)
        
        result.append(min_value)
    
    return result