# 총 테스트 케이스 수 입력
T = int(input())

for t in range(1, T + 1):
    # 사재기 할 수 있는 총 일수
    N = int(input())
    
    # N개의 매매가 입력 받기
    prices = list(map(int, input().split()))
    
    max_profit = 0
    max_price = 0  # 현재까지 본 최대 판매 가격
    
    # 역순으로 매매가를 살펴봅니다.
    for price in reversed(prices):
        if price > max_price:
            max_price = price  # 새로운 최대 가격 업데이트
        max_profit += max_price - price  # 현재 가격과 최대 가격의 차이를 더함
    
    print(f'#{t} {max_profit}')