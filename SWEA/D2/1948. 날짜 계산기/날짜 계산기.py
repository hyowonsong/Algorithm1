# 날짜 계산기

# 각 달의 마지막 날짜
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    
    # 첫 번째 날짜까지의 총 일수 계산
    days1 = sum(month[1:m1]) + d1
    
    # 두 번째 날짜까지의 총 일수 계산
    days2 = sum(month[1:m2]) + d2
    
    # 차이 계산 (당일 포함이므로 +1)
    result = days2 - days1 + 1
    
    print(f'#{t} {result}')