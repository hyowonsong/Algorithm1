from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 모든 가능한 숫자 조합 생성
    nums = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            nums.add(int(''.join(perm)))

    # 소수 개수 세기
    prime_count = 0
    for num in nums:
        if is_prime(num):
            prime_count += 1
    
    return prime_count
