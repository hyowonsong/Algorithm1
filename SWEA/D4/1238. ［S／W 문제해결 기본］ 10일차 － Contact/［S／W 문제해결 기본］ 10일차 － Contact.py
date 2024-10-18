def bfs(s):
    q = []
    v = [0]*101

    q.append(s)
    v[s]=1
    ans = s         # 리턴할 노드번호

    while q:
        c = q.pop(0)
        # 더 늦게 연락받거나  동시에 최종연락이면 큰 값
        if v[ans]<v[c] or (v[ans]==v[c] and ans<c):
            ans = c

        for n in adj[c]:    # 연결된
            if not v[n]:    # 미방문
                q.append(n)
                v[n] = v[c]+1
    return ans

T = 10
# T = int(input())
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i+1]
        adj[p].append(c)

    ans = bfs(S)
    print(f'#{test_case} {ans}')