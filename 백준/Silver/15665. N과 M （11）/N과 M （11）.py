# N과 M(11)

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이 M
# 여기는 S, v[] 둘다 필요없다!

def dfs(n, tlst):
    if n==M:
        ans.append(tlst)
        return

    prev = 0
    for j in range(N):
        if prev!=lst[j]:
            prev = lst[j]
            dfs(n+1, tlst+[lst[j]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
dfs(0, [])

for lst in ans:
    print(*lst)