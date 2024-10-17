
def dfs(n, tlst):
    if n == M:  
        ans.append(tlst)
        return
    
    # 이전에 선택한 숫자를 저장하는 변수 (초기값은 0) 
    prev = 0 
    for j in range(N):
         # 중복된 숫자를 선택하지 않기 위해 체크
        if v[j] == 0 and prev != lst[j]: 
            v[j] = 1 
            dfs(n+1, tlst + [lst[j]]) 
            v[j] = 0 
            # prev 값을 현재 숫자로 갱신
            prev = lst[j]  

N, M = map(int, input().split())
lst = sorted(list(map(int,input().split())))

ans = []
v = [0] * N
dfs(0, [])

for lst in ans:
    print(*lst)