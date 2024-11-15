N = int(input())
lst = list(map(int, input().split()))
alst = [n for n in range(1, N+1)]

for i in range(N):          # i위치의 학생을 순서대로 이동을 처리
    n, t = lst[i], alst[i]  # 앞으로 이동할 칸 수, 학생 번호
    for j in range(i, i-n, -1):
        alst[j] = alst[j-1]
    alst[i-n]=t
print(*alst)