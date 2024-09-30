T = int(input())

coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    N = int(input())  
    result = [] 

    # 화폐 단위별로 필요한 개수 계산
    for coin in coins:
        count = N // coin  
        result.append(count)
        N %= coin  # 남은 금액 업데이트
    

    print(f"#{t}")
    print(*result)