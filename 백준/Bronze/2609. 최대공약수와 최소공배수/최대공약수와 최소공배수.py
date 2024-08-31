n, m = map(int, input().split())

def solution(n, m):
    # 최대공약수 (GCD) 계산
    arr1 = []
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            arr1.append(i)
    
    # 최소공배수 (LCM) 계산
    for i in range(max(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            min_num = i
            break
    
    max_num = max(arr1)
    
    print(max_num)
    print(min_num)

solution(n, m)
