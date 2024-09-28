
T = int(input())

# 테스트 케이스 반복
for t in range(1, T + 1):
    # 10개의 수 입력
    numbers = list(map(int, input().split()))

    # 평균값 계산
    average = round(sum(numbers) / len(numbers))  

    # 결과 출력
    print(f'#{t} {average}')  
