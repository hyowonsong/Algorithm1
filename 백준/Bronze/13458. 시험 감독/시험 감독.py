n = int(input())
lst = list(map(int,input().split()))
B,C = map(int, input().split())

# 총감독관의 시험장의 개수만큼
answer = n
for n in lst:
    if n-B>0:
        answer += (n-B+C-1)//C
print(answer)
