T = int(input()) 

for t in range(1, T + 1):
    N, K = map(int, input().split())  
    items = []  

    # N개의 물건에 대한 부피와 가치를 입력받음
    for _ in range(N):
        Vi, Ci = map(int, input().split())
        items.append((Vi, Ci))
    
    
    dp = [0] * (K + 1)

   
    for Vi, Ci in items:
        for j in range(K, Vi - 1, -1):
            dp[j] = max(dp[j], dp[j - Vi] + Ci)

    # 결과 출력
    print(f'#{t} {dp[K]}')
