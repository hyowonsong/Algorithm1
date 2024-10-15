n, m = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = 0

# 카드 3장을 선택하기 위해 세 개의 인덱스를 사용
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            current_sum = numbers[i] + numbers[j] + numbers[k]
            
            # 현재 합이 M을 넘지 않으면서 최대값을 업데이트
            if current_sum <= m:
                max_sum = max(max_sum, current_sum)

print(max_sum)
