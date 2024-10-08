# 통계학
import sys
input=sys.stdin.readline


# 입력 받기
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 산술 평균
arithmetic_mean = round(sum(numbers) / N)

# 중앙값
numbers.sort()
median = numbers[N // 2]

# 최빈값
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# 최빈값을 구하기
max_count = max(frequency.values())
mode_candidates = [num for num, count in frequency.items() if count == max_count]
mode_candidates.sort()  # 최빈값 후보들을 정렬

# 두 번째로 작은 값을 선택
if len(mode_candidates) > 1:
    mode = mode_candidates[1]  # 두 번째로 작은 값
else:
    mode = mode_candidates[0]  # 최빈값 후보가 하나일 경우

# 범위
range_value = max(numbers) - min(numbers)

# 결과 출력
print(arithmetic_mean)
print(median)
print(mode)
print(range_value)
