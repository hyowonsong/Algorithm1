def solution(x):
    # x의 자릿수의 합을 계산합니다.
    new = str(x)
    digit_sum = 0

    for digit in new:
        digit_sum += int(digit)
    
    # x가 그 자릿수의 합으로 나누어지는지 확인합니다.
    if x % digit_sum == 0:
        return True
    else:
        return False
    