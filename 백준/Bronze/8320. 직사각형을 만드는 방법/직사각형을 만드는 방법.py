# 직사각형을 만드는 방법

N = int(input())

# [1] 가능한 경우를 모두 순회
ans = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        if i*j <= N:
            ans += 1
print(ans)