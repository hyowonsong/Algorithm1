# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    # N과 M 입력
    N, M = map(int, input().split())
    
    # N x N 배열 입력
    fly_count = [list(map(int, input().split())) for _ in range(N)]
    
    max_flies = 0  # 최대 파리 수 초기화

    # M x M 파리채를 놓을 수 있는 모든 위치 검사
    for i in range(N - M + 1):  # 행
        for j in range(N - M + 1):  # 열
            current_flies = 0
            for k in range(M):  
                for l in range(M):
                    current_flies += fly_count[i + k][j + l]
            # 최대값 업데이트
            max_flies = max(max_flies, current_flies)

    # 결과 
    print(f"#{t} {max_flies}")
