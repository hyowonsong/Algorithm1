def solution(number, limit, power):
    answer = 0
    divisor_count = [0] * (number + 1)  # 기사들의 약수 개수를 저장할 리스트 초기화
    
    # 각 기사들의 번호에 따른 약수의 개수 계산
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisor_count[j] += 1
    
    # 각 기사들이 구매할 무기의 공격력에 따라 필요한 철의 무게 계산
    for count in divisor_count[1:]:
        if count <= limit:  # 제한수치 이내의 공격력을 가진 무기를 구매할 경우
            answer += count
        else:  # 제한수치를 초과한 공격력을 가진 무기를 구매할 경우
            answer += power
            
    return answer