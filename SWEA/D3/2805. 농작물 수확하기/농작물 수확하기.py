
T = int(input())
for t in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    # 마름모 형태를 계산
    total = 0
    # 중앙
    mid = n // 2

    for i in range(n): 
        # 현재 행 i와 중앙 행(mid) 사이의 거리를 계산합니다.
        start = abs(mid - i)  
        # 수확할 범위의 끝 인덱스를 계산합니다.
        end = n - start  
        
        # 수확할 범위의 열을 순회합니다.
        for j in range(start, end):  
            # 현재 열의 농작물 가치를 total에 추가합니다.
            total += graph[i][j]  

    print(f'#{t} {total}')