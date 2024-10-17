# N과 M(5)

def dfs(n,tlst):
    if n == M:
        ans.append(tlst)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, tlst + [lst[j]])
            v[j] = 0


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = []
v = [0] * N
dfs(0, [])

for lst in ans:
    print(*lst)