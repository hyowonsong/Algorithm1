# 어디에 단어가 들어갈 수 있을까

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    
    graph = [list(map(int,input().split())) for _ in range(N)]

    count = 0

    # 가로 검사
    for i in range(N):
        length = 0  # 연속된 1의 길이
        for j in range(N):
            if graph[i][j] == 1:
                length += 1
            else:
                if length == M:  # 길이가 M인 경우 자리를 셈
                    count += 1
                length = 0  # 0이 나오면 길이 초기화
        if length == M:  # 마지막 칸까지 연속된 경우도 검사
            count += 1
    
    # 세로 검사
    for j in range(N):
        length = 0  # 연속된 1의 길이
        for i in range(N):
            if graph[i][j] == 1:
                length += 1
            else:
                if length == M:  # 길이가 K인 경우 자리를 셈
                    count += 1
                length = 0  # 0이 나오면 길이 초기화
        if length == M:  # 마지막 칸까지 연속된 경우도 검사
            count += 1
    
    # 결과 출력
    print(f'#{t} {count}')