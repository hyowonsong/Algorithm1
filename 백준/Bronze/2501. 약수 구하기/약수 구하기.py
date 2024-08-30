def divisor(n, k):
    divisors_set = set()

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors_set.add(i)
            divisors_set.add(n // i)

    # 약수들을 정렬
    sorted_divisors = sorted(divisors_set)

    # K번째 약수 출력
    if k <= len(sorted_divisors):
        return sorted_divisors[k - 1]
    else:
        return 0

# 입력 받기
n, k = map(int, input().split())
print(divisor(n, k))
