def solution(arr1, arr2):
    # arr1의 행의 개수 m, 열의 개수 n
    m = len(arr1)
    n = len(arr1[0])
    
    # arr2의 행의 개수는 n, 열의 개수는 p
    p = len(arr2[0])
    
    # 결과 행렬 C 초기화
    result = [[0] * p for _ in range(m)]
    
    # 행렬 곱셈 계산
    for i in range(m):       # C의 행 인덱스 i
        for j in range(p):   # C의 열 인덱스 j
            for k in range(n):  # A[i][k]와 B[k][j]를 곱해줌
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result