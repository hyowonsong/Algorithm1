T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    ans = set()

    # 세 개의 숫자를 골라 합을 구함
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                sum_val = numbers[i] + numbers[j] + numbers[k]
                ans.add(sum_val)  # 합을 집합에 추가하여 중복 제거

    # 정렬 후 내림차순으로 5번째로 큰 값 선택
    result = sorted(ans, reverse=True)

    print(f'#{t} {result[4]}') 