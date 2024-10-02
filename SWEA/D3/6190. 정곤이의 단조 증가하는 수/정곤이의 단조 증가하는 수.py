T = int(input())  

for t in range(1, T + 1):
    n = int(input())  
    numbers = list(map(int, input().split()))  
    
    max_number = -1 

    # 모든 가능한 두 숫자의 곱 계산
    for i in range(n):
        for j in range(i + 1, n):
            product = numbers[i] * numbers[j]  
            
            # 단조 증가 여부를 확인하는 과정 
            product_str = str(product)  # 곱한 결과를 문자열로 변환
            # 초기값을 단조 증가로 설정
            monotonic = True  
            for k in range(len(product_str) - 1):
                if product_str[k] > product_str[k + 1]:  # 앞자리 숫자가 뒷자리보다 크면 단조 증가 아님
                    monotonic = False
                    break

            # 단조 증가하는 경우 최댓값 갱신
            if monotonic:
                if product > max_number:
                    max_number = product

    # 결과 출력
    print(f'#{t} {max_number}')