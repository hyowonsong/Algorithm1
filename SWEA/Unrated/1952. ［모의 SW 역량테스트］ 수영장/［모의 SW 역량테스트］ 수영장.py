
def dfs(n, sm):
    global ans
    # if ans<=sm:
    #     return
    # 여기 n 이 12보다 커야 한다고 적은 것이 종료조건!
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
    # 각 달의 이용 계획을 입력받고, lst[1]부터 12까지 사용할 수 있도록 앞에 0을 추가
    lst = [0] + list(map(int, input().split()))
    # 최소 비용을 저장하기 위한 ans 변수를 초기화
    ans = 300*12
    # DFS 탐색 시작 (1월부터 시작, 현재 비용은 0)
    dfs(1, 0)
 
    print(f'#{test_case} {ans}')