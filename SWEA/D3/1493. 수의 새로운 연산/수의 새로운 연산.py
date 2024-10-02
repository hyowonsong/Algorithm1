T = int(input())

for t in range(1, T + 1):
    p, q = map(int, input().split())

    # n_p 를 1로 초기화. 이는 p에 해당하는 점의 대각선 번호
    n_p = 1
    # p 가 위치하는 대각선 번호 찾기, 대각선 n_p 의 마지막 점의 번호 계산
    while (n_p * (n_p + 1)) // 2 < p:
        n_p += 1
    
    # idx_p 는 대각선 n_p 에서 p의 위치를 계산, 대각선 n_p-1 까지의 점 개수 빼줌
    idx_p = p - (n_p * (n_p - 1)) // 2
    x1 = idx_p
    y1 = n_p - idx_p + 1

    # q 가 위치하는 대각선 번호 찾기, q에 해당하는 점의 대각선 번호 찾기
    n_q = 1
    while (n_q * (n_q + 1)) // 2 < q:
        n_q += 1
    
    # idx_q는 대각선 n_q에서 q의 위치를 계산, 대각선 n_q-1까지의 점의 개수를 빼줌
    idx_q = q - (n_q * (n_q - 1)) // 2
    x2 = idx_q
    y2 = n_q - idx_q + 1

    x_sum = x1 + x2
    y_sum = y1 + y2
    
    # 두 점의 대각선 번호를 계산
    n_sum = x_sum + y_sum - 1
    result = (n_sum * (n_sum + 1)) // 2 - (y_sum - 1)

    print(f'#{t} {result}')