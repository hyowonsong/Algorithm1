def dfs(n, s, tlst):
    # 종료조건: 6개의 숫자 선택한 경우
    if n==6:    
        ans.append(tlst)
        return

    for j in range(s, N):
        dfs(n+1, j+1, tlst+[lst[j]])

while True:
    lst_in = list(map(int, input().split()))
    # 입력 종료
    if lst_in[0]==0:    
        break

    N = lst_in[0]
    lst = lst_in[1:]

    ans = []
    dfs(0, 0, [])

    for lst in ans:
        print(*lst)
    print()