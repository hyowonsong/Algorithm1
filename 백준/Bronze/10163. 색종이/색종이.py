N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):   # 해당 번호 색종이 숫자를 영역에 표시
            arr[i][j]=n
        

# [2] cnts: 빈도수 배열 사용해서, arr한 번만 순회
cnts = [0]*(N+1)
for lst in arr:
    for n in lst:
        cnts[n] += 1
for cnt in cnts[1:]:
    print(cnt)