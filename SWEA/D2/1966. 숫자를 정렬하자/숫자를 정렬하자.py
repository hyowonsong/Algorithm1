# 숫자를 정렬하자

# 주어진 N 길의 숫자열을 오름차순으로 정렬하여 출력
T = int(input())

for t in range(1,T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    numbers.sort()

    print(f'#{t}', ' '.join(map(str,numbers)))