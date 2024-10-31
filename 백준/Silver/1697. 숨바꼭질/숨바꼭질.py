# 1697 숨바꼭질

# 수빈이는 현재점 N, 동생은 점 K
# 걷기 -> x-1, x+1
# 순간이동 -> 2*x의 위치

from collections import deque
n, k = map(int, input().split())
dq = [0] * 1000001

def bfs(v):
    q = deque([v]) #큐 구현을 위해 deque 사용
    while q:      # q가 빌때까지 계속 돈다
        v = q.popleft()
        if v == k:
            return dq[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not dq[i]:
                dq[i] = dq[v] + 1
                q.append(i)

print(bfs(n))