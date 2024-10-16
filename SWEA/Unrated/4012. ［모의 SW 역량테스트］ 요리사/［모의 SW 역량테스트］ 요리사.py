def dfs(n, alst, blst):
    global ans
    if n==N:
        if len(alst) == M:  # a음식에 선택된 재료 개수가 절반일 경우
            asum = bsum = 0 # 음식맛의 합 구하기
            for i in range(M):
                for j in range(M):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asum-bsum))
        return
 
    dfs(n+1, alst+[n], blst)    # a음식에 추가
    dfs(n+1, alst, blst+[n])    # b음식에 추가
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = N//2
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000*N*N
 
    dfs(0, [], [])
    print(f'#{test_case} {ans}')