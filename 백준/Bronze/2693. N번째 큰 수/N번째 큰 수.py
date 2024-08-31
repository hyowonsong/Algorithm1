import sys

input = sys.stdin.readline

# 첫 번째 입력: 숫자의 개수
n = int(input().strip())

for i in range(n):
    # 각 줄에서 숫자들을 읽어오고 정렬
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    print(numbers[-3])