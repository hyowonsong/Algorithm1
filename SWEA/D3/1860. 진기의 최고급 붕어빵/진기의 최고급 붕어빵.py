T = int(input())  

for t in range(1, T + 1):
    # N: 손님의 수, M: 붕어빵 만드는 데 걸리는 시간, K: M초마다 만드는 붕어빵의 수
    N, M, K = map(int, input().split())
    
    # 각 손님이 도착하는 시간 입력
    arrival_times = list(map(int, input().split()))
    
    # 도착 시간 순으로 정렬
    arrival_times.sort()
    
    # 가능 여부를 저장할 변수
    possible = True  
    
    for i in range(N):
        # 현재 손님이 도착할 시각
        current_time = arrival_times[i]
        
        # current_time까지 만든 붕어빵의 수 = (current_time // M) * K
        made_bread = (current_time // M) * K
        
        # i + 1명이 현재까지 도착했으므로 그만큼 붕어빵이 있어야 함
        if made_bread < i + 1:
            possible = False
            break
    
    # 결과 출력
    if possible:
        print(f"#{t} Possible")
    else:
        print(f"#{t} Impossible")