# DFS 함수를 정의
def dfs(n, num, ci, cj):
    # 만약 이동 횟수가 CNT(7)와 같아지면, 생성된 숫자를 집합에 추가
    if n == CNT:
        sset.add(num)  # 중복을 허용하지 않는 집합에 추가
        return
    
    # 상하좌우로 이동하기 위한 방향 배열
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        # 현재 위치에서 새로운 위치 계산    
        ni, nj = ci + di, cj + dj
        # 새로운 위치가 격자판 내에 있는지 확인
        if 0 <= ni < N and 0 <= nj < N:
            # DFS를 재귀적으로 호출, n(이동 횟수) + 1, 생성된 숫자는 num을 10배하여 새 숫자를 이어붙임
            dfs(n + 1, num * 10 + arr[ni][nj], ni, nj)


T = int(input())
for test_case in range(1, T + 1):
    # 격자판의 크기(N)와 만들어야 할 숫자의 자리 수(CNT)를 설정
    N, CNT = 4, 7  
    # 격자판 입력받기
    arr = [list(map(int, input().split())) for _ in range(N)]  

    # 중복된 수를 저장하지 않는 집합을 초기화
    sset = set()  
    for si in range(N): 
        for sj in range(N): 
            # 각 위치(si, sj)에서 DFS 시작
            dfs(1, arr[si][sj], si, sj)

 
    print(f'#{test_case} {len(sset)}')  