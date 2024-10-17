# N과 M(10)

# 비내림차순
# 중복되는 수열은 여러 번 출력하면 안된다.

def dfs(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return
    
    prev = 0
    for j in range(s, N):
        if v[j] == 0 and prev != lst[j]:
            v[j] = 1
            dfs(n+1, j+1, tlst + [lst[j]])
            v[j] = 0
            prev = lst[j]

N, M = map(int,input().split())
lst = sorted(list(map(int, input().split())))


ans = []
v = [0] * N
dfs(0, 0, [])

for lst in ans:
    print(*lst)