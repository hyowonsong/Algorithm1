
T = int(input())  

for t in range(1, T+1):
    n = input().strip()  

    if n == n[::-1]:  
        print(f'#{t} 1')
    else: 
        print(f'#{t} 0')