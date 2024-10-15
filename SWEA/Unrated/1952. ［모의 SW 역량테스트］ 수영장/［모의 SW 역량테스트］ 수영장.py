def dfs(n, sm):
    global ans
    if ans<=sm:
        return
 
    if n>12:
        ans = min(ans, sm)
        return
 
    dfs(n+1, sm+day*lst[n]) # 일간권
    dfs(n+1, sm+mon)        # 월간권
    dfs(n+3, sm+mon3)       # 분기권
    dfs(n+12, sm+year)      # 년간권
 
T = int(input())
for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    ans = 3000*12
    dfs(1, 0)
 
    print(f'#{test_case} {ans}')