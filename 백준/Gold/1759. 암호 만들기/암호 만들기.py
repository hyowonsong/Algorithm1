def dfs(n, cnt, tst):
    if n == C:    
        # 암호 길이가 L이며, 모음 개수가 1개 이상, 자음 개수가 2개 이상인 경우
        if len(tst) == L and cnt >= 1 and L - cnt >= 2:
            ans.append(tst)  
        return

    # 현재 알파벳을 포함하는 경우를 탐색
    dfs(n + 1, cnt + tbl[ord(lst[n])], tst + lst[n])  
    # 현재 알파벳을 포함하지 않는 경우도 탐색
    dfs(n + 1, cnt, tst)                          

L, C = map(int, input().split())
lst = sorted(input().split())
# 아스키코드는 총 128개이므로 128개 크기의 리스트를 만듦
tbl = [0] * 128
# 모음인 알파벳 'a, e, i, o, u'의 아스키 값을 이용해 tbl에 1을 기록
for ch in "aeiou":
    tbl[ord(ch)] = 1

ans = []
# DFS 탐색 시작: 초기 n=0, cnt=0, tst=""
dfs(0, 0, "")

for st in ans:
    print(st)