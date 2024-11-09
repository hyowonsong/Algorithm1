# 11315 오목 판정

def solve():
    for si in range(N):
        for sj in range(N):  # 모든 좌표 순회
            for di, dj in ((0, 1), (1, 0), (1, 1), (-1, 1)):
                found_five = True  # 5개의 연속된 돌이 있는지 확인하는 변수
                
                for mul in range(5):
                    ni, nj = si + di * mul, sj + dj * mul
                    # 범위를 벗어나거나 돌이 없는 경우
                    if not (0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o'):
                        found_five = False
                        break

                # 5개의 연속된 돌을 발견한 경우
                if found_five:
                    return 'YES'
    
    # 모든 좌표와 방향을 확인했으나 오목이 없으면 'NO' 반환
    return 'NO'
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
 
    ans = solve()
 
    print(f'#{test_case} {ans}')
            