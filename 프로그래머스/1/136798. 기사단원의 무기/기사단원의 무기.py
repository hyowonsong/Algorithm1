# 기사단원의 무기

def solution(number, limit, power):
    answer = 0

    # 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
    # 제한수치보다 큰 공경력을 가진 무기를 구매해야 하는 기사는 기관에서 정한 무기 구매해야

    def count_divisor(n):
        count = 0 
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                count += 1
                # i != n // i는 i가 n의 제곱근이 아닐 때 두 개의 약수 (i와 n // i)를 모두 계산하고, 
                # 제곱근인 경우에는 중복 계산을 방지하기 위해 한 번만 계산
                if i != n//i:
                    count += 1
        return count
    
    total_weight = 0
    for i in range(1,number+1):
        divisors_count = count_divisor(i)
        if divisors_count > limit:
            total_weight += power
        else:
            total_weight += divisors_count

    return total_weight
