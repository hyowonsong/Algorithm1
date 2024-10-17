def dfs(n, tlst):
    if n==M:
        ans.append(tlst)
        return

    for j in range(N):
        dfs(n+1, tlst+[lst[j]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
dfs(0, [])

for lst in ans:
    print(*lst)