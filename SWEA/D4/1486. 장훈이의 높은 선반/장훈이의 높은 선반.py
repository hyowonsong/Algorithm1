def dfs(n, sm):
    global ans
    if n == N:
        if sm>=B:
            ans = min(ans, sm-B)
        return
    
    # 포함하는 경우
    dfs(n+1, sm+lst[n])
    # 포함하지 않는 경우
    dfs(n+1,sm)

T = int(input())
for test_case in range(1,T + 1):
    # N은 개수, B는 점원들 키의 합이 이것보다는 커야
    N, B = map(int,input().split())
    lst = list(map(int, input().split()))

    # 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것 출력
    ans = N*10000
    dfs(0,0)
    print(f'#{test_case} {ans}')