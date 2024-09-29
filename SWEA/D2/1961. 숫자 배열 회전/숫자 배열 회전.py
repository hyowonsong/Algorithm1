T = int(input())

for t in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 90도, 180도, 270도 회전된 결과를 저장할 리스트
    rotate_90 = [[0] * N for _ in range(N)]
    rotate_180 = [[0] * N for _ in range(N)]
    rotate_270 = [[0] * N for _ in range(N)]
    
    # 회전 계산
    for i in range(N):
        for j in range(N):
            rotate_90[j][N-1-i] = matrix[i][j]     # 90도 회전
            rotate_180[N-1-i][N-1-j] = matrix[i][j] # 180도 회전
            rotate_270[N-1-j][i] = matrix[i][j]    # 270도 회전
    
    
    print(f'#{t}')
    for i in range(N):
        # 회전된 행렬들 중 같은 행끼리 출력
        print(''.join(map(str, rotate_90[i])), ''.join(map(str, rotate_180[i])), ''.join(map(str, rotate_270[i])))