# 행렬의 곱셈

def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    
    # 맨 처음 행렬 배열 초기화
    result = []
    for i in range(n):
        # arr2의 열 개수만큼 0으로 초기화된 리스트 생성
        row = []
        for j in range(m):
            row.append(0)
        # 생성된 행(row)을 결과 리스트에 추가    
        result.append(row)

    # 행렬 곱셈 수행
    for i in range(n):
        for j in range(m):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result