# 행렬의 곱셈

def solution(arr1, arr2):
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(r)] for _ in range(m)] # m * r 크기의 행렬

    for i in range(m):
        for k in range(r):
            for j in range(n):
                answer[i][k] += arr1[i][j] * arr2[j][k]
    return answer