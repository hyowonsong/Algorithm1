
T = int(input())
for t in range(1, T+1):
    N = input()
    n = len(N)
    min_val = int(N)
    max_val = int(N)
    
    # 모든 가능한 자리 쌍에 대해 교환 시도
    for i in range(n):
        for j in range(i+1, n):
            # 숫자들을 리스트로 변환하여 교환
            num_list = list(N)
            num_list[i], num_list[j] = num_list[j], num_list[i]
            
            # 첫 자리가 0이 아닌 경우만 고려
            if num_list[0] != '0':
                new_num = int(''.join(num_list))
                min_val = min(min_val, new_num)
                max_val = max(max_val, new_num)
    
    print(f"#{t} {min_val} {max_val}")