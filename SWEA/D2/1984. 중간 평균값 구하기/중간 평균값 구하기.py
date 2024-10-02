T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()

    total = 0
    count = 0

    for num in numbers[1:-1]:  # 최대값과 최소값을 제외한 부분
        total += num
        count += 1

    median = round(total / count)  # 평균값 계산 및 반올림

    print(f'#{t} {median}')  # 결과 출력