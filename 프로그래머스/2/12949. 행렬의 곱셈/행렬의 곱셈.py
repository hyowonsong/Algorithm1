# 행렬의 곱셈

def solution(arr1, arr2):
    # 2차원 행렬 arr1과 arr2 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수
    # 행 먼저
    m = len(arr1)
    # 열
    n = len(arr1[0])

    # arr2의 행의 개수는 n, 열의 개수는 p (이거 해줘야)
    p = len(arr2[0])

    # 행렬 초기화
    result = [] 
    for _ in range(m):
        result.append([0]*p)

    # 곱셈 수행
    for i in range(m):
        for j in range(p):
            for k in range(n):
                # 여기 +로 계속 누적해줘야
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result