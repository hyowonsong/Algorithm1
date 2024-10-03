def cnt(N, K, arr, idx=0, cur_sum=0):
    # 종료 조건: 리스트의 끝에 도달했을 때
    if idx == N:
        if cur_sum == K:
            return 1  
        else:
            return 0
    
    # 현재 숫자를 선택하지 않은 경우와 선택한 경우를 모두 탐색
    skip = cnt(N, K, arr, idx + 1, cur_sum)
    take = cnt(N, K, arr, idx + 1, cur_sum + arr[idx])
    
    # 두 경우의 수를 더한 값을 반환
    return skip + take


T = int(input())  

for t in range(T):
    N, K = map(int, input().split())  
    arr = list(map(int, input().split())) 
    
    result = cnt(N, K, arr)  # 부분 수열의 합이 K인 경우의 수 계산
    
    print(f'#{t + 1} {result}')