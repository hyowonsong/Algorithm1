# 최대수 구하기

n = int(input())

for i in range(1, n+1):
    a = map(int, input().split())  
    max_value = max(a)  

    print(f'#{i} {max_value}')  
