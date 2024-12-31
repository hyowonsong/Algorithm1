# 행렬의 곱셈

def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2[0])
    
    # arr1의 행 개수만큼 반복
    result = []
    for i in range(m):
        # arr2의 열 개수만큼 0으로 초기화된 리스트 생성
        row = []
        for j in range(n):
            row.append(0)
        # 생성된 행(row)을 결과 리스트에 추가    
        result.append(row)

    # 행렬 곱셈 수행
    for i in range(m):
        for j in range(n):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result