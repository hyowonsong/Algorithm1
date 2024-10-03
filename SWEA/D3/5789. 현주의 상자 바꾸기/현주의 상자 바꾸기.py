T = int(input())

for t in range(1, T + 1):
    N, Q = map(int, input().split())  
    boxes = [0] * N
    
    for i in range(1, Q + 1):
        # i번째 작업에 대한 L, R 값
        L, R = map(int, input().split())  
        # 인덱스가 0부터 시작하므로 L-1부터 R까지 범위 지정
        for j in range(L - 1, R):
            # 해당 범위의 상자를 i로 변경  
            boxes[j] = i  
    
    # 결과 출력
    print(f'#{t}', *boxes)