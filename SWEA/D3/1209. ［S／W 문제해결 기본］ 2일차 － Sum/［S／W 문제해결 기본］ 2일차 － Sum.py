# 2일차 - Sum

# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램 작성

T = 10
for t in range(1, T + 1):
    n = int(input().strip())
    
    array = [list(map(int, input().strip().split())) for _ in range(100)]
    
    max_sum = 0  

    # 각 행의 합 계산
    for i in range(100):
        row_sum = sum(array[i])
        max_sum = max(max_sum, row_sum)  # 최대 합 갱신

    # 각 열의 합 계산
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += array[i][j]
        max_sum = max(max_sum, col_sum)  # 최대 합 갱신

    # 주 대각선의 합 계산
    diag1_sum = 0
    for i in range(100):
        diag1_sum += array[i][i]  
    max_sum = max(max_sum, diag1_sum)  # 최대 합 갱신

    # 부 대각선의 합 계산
    diag2_sum = 0
    for i in range(100):
        diag2_sum += array[i][99 - i]  # (0,99), (1,98), ..., (99,0)
    max_sum = max(max_sum, diag2_sum)  # 최대 합 갱신

    # 결과 출력
    print(f'#{n} {max_sum}')
