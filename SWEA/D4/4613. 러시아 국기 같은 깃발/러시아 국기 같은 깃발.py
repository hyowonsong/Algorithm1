# 러시아 국기 같은 깃발

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 행의 개수(N)와 열의 개수(M)
    arr = [input() for _ in range(N)]  # 깃발 색상 배열

    mx = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            # i+1까지 흰색으로 칠하기 위한 칸 수 세기
            for s in range(i+1):
                cnt += arr[s].count('W')
            # i+1부터 j+1까지 파란색으로 칠하기 위한 칸 수 세기
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            # j+1부터 N까지 빨간색으로 칠하기 위한 칸 수 세기
            for s in range(j+1, N):
                cnt += arr[s].count('R')
            # 최대한 맞춘 칸의 개수 업데이트
            mx = max(mx, cnt)

    print(f'#{tc} {N*M - mx}')  # 전체 칸 수에서 mx를 빼서 최소 칠해야 하는 칸 수 계산


