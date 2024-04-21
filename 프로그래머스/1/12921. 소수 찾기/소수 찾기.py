def solution(n):
    prime_count = 0  # 소수 개수를 저장할 변수 초기화

    for i in range(2, n+1):  # 2부터 n까지의 숫자에 대해 반복
        is_prime = True  # 현재 숫자가 소수인지 여부를 나타내는 변수 초기화

        for j in range(2, int(i**0.5) + 1):  # 2부터 i의 제곱근까지의 숫자에 대해 반복
            if i % j == 0:  # i가 j로 나누어지면 소수가 아님
                is_prime = False
                break

        if is_prime:  # is_prime이 True면 현재 숫자는 소수
            prime_count += 1  # 소수 개수를 1 증가시킴

    return prime_count  # 소수의 개수 반환