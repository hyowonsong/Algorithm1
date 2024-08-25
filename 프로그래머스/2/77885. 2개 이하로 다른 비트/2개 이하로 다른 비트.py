def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:  # 짝수일 경우
            answer.append(number + 1)
        else:  # 홀수일 경우
            # 가장 오른쪽의 0을 1로 바꾸고, 그 다음 비트를 0으로 변경합니다.
            # 이 방법은 number와 number+1을 비트 OR 연산하여 다음 큰 수를 찾고,
            # 이를 number와 비트 XOR 연산으로 차이를 2로 줄입니다.
            bit = 1
            while number & bit:  # 가장 오른쪽의 0을 찾을 때까지 이동
                bit <<= 1
            # 해당 0 비트를 1로 바꾸고, 그 다음 비트를 0으로 바꿉니다.
            answer.append(number + bit - (bit >> 1))
    
    return answer
