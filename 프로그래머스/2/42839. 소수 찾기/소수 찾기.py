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
        # numbers에서 i개의 숫자를 선택하여 만들 수 있는 모든 순열 생성
        perms = permutations(numbers, i)
        for perm in perms:
            # 각 순열을 정수로 변환하여 집합에 추가
            # set을 사용하여 중복 제거
            nums.add(int(''.join(perm)))

    # 소수 개수 세기
    count = 0
    for num in nums:
        # 각 숫자에 대해 소수 여부 확인
        if is_prime(num):
            # 소수일 경우 카운트 증가
            count += 1

    # 찾은 소수의 개수 반환
    return count
