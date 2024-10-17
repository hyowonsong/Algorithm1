def dfs(n,s,lst):
    if n == M:
        ans.append(lst)
        return
    
    # 고른 수열은 비내림차순
    for j in range(s,N+1):
        dfs(n+1, j, lst+[j])

N,M = map(int, input().split())
ans = []
dfs(0,1,[])
for lst in ans:
    print(*lst)
