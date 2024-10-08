# 행렬 곱셈

# N*M 크기의 행렬 A와 M*K 크기의 행렬 B 곱하기
N, M = map(int, input().split())

# A 행렬 입력
A = [list(map(int, input().split())) for _ in range(N)]

# M*K 크기 (M은 A의 열 수와 동일해야 함)
M, K = map(int, input().split())

# B 행렬 입력
B = [list(map(int, input().split())) for _ in range(M)]

# 결과 행렬 초기화
result = [[0] * K for _ in range(N)]

# 행렬 곱셈
for i in range(N):          # A의 행
    for j in range(K):      # B의 열
        for k in range(M):   # A의 열(=B의 행)
            result[i][j] += A[i][k] * B[k][j]

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))
