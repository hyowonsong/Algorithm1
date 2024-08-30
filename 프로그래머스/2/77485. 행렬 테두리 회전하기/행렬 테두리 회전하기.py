def solution(rows, columns, queries):
    # 행렬 초기화
    matrix = []

    # rows만큼 반복하여 각 행을 생성합니다.
    for i in range(rows):
        # 각 행을 저장할 빈 리스트를 생성합니다.
        row = []
        # columns만큼 반복하여 각 열의 값을 추가합니다.
        for j in range(columns):
            # 각 열의 값을 0으로 초기화하여 추가합니다.
            row.append(0)
        # 생성된 행을 matrix에 추가합니다.
        matrix.append(row)
        
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * columns + j + 1
    
    result = []
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1  # 0-based 인덱스로 변환
        
        # 회전할 요소들을 저장
        temp = matrix[x1][y1]
        min_value = temp
        
        # 왼쪽 세로줄
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i+1][y1]
            min_value = min(min_value, matrix[i][y1])
        
        # 아래쪽 가로줄
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i+1]
            min_value = min(min_value, matrix[x2][i])
        
        # 오른쪽 세로줄
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i-1][y2]
            min_value = min(min_value, matrix[i][y2])
        
        # 위쪽 가로줄
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i-1]
            min_value = min(min_value, matrix[x1][i])
        
        matrix[x1][y1+1] = temp
        
        result.append(min_value)
    
    return result
