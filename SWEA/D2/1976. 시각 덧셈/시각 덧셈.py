T = int(input())

# 각 테스트 케이스를 처리
for t in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    
    total_hours = h1 + h2
    total_minutes = m1 + m2
    
    # 분이 60 이상이면 시로 1시간을 올리고, 분을 60으로 나눈 나머지를 구함
    if total_minutes >= 60:
        total_hours += 1
        total_minutes -= 60
    
    # 시가 12를 초과하면 12시간제로 변환 
    if total_hours > 12:
        total_hours -= 12
    

    print(f'#{t} {total_hours} {total_minutes}')
