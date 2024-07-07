def solution(n):
    answer = 0  

    for i in range(2, n+1):  # 2부터 n까지의 숫자에 대해 반복
        is_prime = True  # 현재 숫자가 소수인지 여부를 판단
        for j in range(2, int(i**0.5) + 1):  
            if i % j == 0:  # i가 j로 나누어지면 소수가 아님
                is_prime = False
                break

        if is_prime:  # is_prime이 True면 현재 숫자는 소수
            answer += 1  # 소수 개수를 1 증가시킴

    return answer 