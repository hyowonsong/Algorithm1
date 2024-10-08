N, K = map(int, input().split())

# N까지의 수를 담는 배열
is_prime = [True] * (N + 1)

count = 0

# 2부터 N까지 소수의 배수를 지우는 과정
for i in range(2, N + 1):
    if is_prime[i]:  
        for multiple in range(i, N + 1, i):
            # multiple이 아직 지워지지 않았으면
            if is_prime[multiple]:  
                # multiple을 지운다
                is_prime[multiple] = False  
                count += 1

                if count == K:
                    print(multiple)
                    break
        
        if count == K:  # 바깥 for문을 멈추기 위해 확인
            break
