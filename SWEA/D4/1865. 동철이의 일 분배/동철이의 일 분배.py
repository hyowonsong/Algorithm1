
def dfs(n, sm):
    global ans
    if ans>=sm:
        return
    if n==N:
        ans = max(ans, sm)
        return

    for j in range(N):
        if not v[j]:
            v[j]=1
            dfs(n+1, sm*(arr[n][j]/100))
            v[j]=0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    v = [0]*N
    dfs(0, 100)
    
    print(f'#{test_case} {ans:.6f}')