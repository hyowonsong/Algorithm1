# 기사단원의 무기

def solution(number, limit, power):
    # 각 기사는 자신의 번호의 약수 개수에 해당하는 무기 구매
    # 제한수치보다 큰 공격력 무기 구매해야 하는 기사는 max_limit 무기 구매
    # 약수 구하는 과정
    def divisor(n):
        count = 0 
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                count += 1
                # i != n // i는 i가 n의 제곱근이 아닐 때 두 개의 약수 (i와 n // i)를 모두 계산하고, 
                # 제곱근인 경우에는 중복 계산을 방지하기 위해 한 번만 계산
                # 16의 약수 구할 때 4는 나누어도 4니까 추가로 count 추가해주지 않는다.
                if i != n//i:
                    count += 1
        return count
    
    answer = 0
    # 여기서도 반드시 1부터 체크해야 한다!!
    for i in range(1,number+1):
        divisors_count = divisor(i)
        # 약수의 개수가 제한 수치(limit)를 초과한다면 power라는 무기를 사용해야
        if divisors_count > limit:
            answer += power
        # 약수의 개수가 초과하지 않는다면 divisors_count를 사용한다.
        else:
            answer += divisors_count

    return answer
