# 소수 만들기

# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    # 3중 반복문으로 숫자 세 개를 선택
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer += 1

    return answer

print(solution([1,2,3,4]))