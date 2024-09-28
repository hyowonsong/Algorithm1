# 점수 개수 입력
N = int(input())

scores = list(map(int, input().split()))


scores.sort()

# 중간값 계산 
median = scores[N // 2]

print(median)