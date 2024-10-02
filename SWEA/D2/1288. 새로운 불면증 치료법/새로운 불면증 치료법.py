T = int(input())

for t in range(1, T + 1):
    N = int(input())
    
    # 지금까지 본 숫자들을 저장할 집합
    seen_digits = set()  
    count = 0            

    # 모든 숫자를 봤는지 확인
    while len(seen_digits) < 10:  
        count += 1
        current_number = N * count  # N의 배수 계산
        seen_digits.update(str(current_number))  # 현재 숫자의 자릿수를 집합에 추가

    print(f"#{t} {current_number}")