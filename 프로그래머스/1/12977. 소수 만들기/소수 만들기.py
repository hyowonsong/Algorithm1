# 소수 만들기(아리스토테네스의 체 사용)
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수

def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

def solution(nums):
    from itertools import combinations
    count = 0
    for comb in combinations(nums, 3):    # combinations를 3개씩
        if is_prime(sum(comb)):           # 만약 소수라면
            count += 1
    return count