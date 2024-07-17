def solution(storey):
    answer = 0  # 필요한 마법의 돌 개수를 저장할 변수
    
    while storey:  # storey가 0이 될 때까지 반복
        digit = storey % 10  # 현재 처리할 자릿수 (1의 자리부터 시작)
        next_digit = (storey // 10) % 10  # 다음으로 높은 자릿수
        
        # 현재 자릿수가 5보다 크거나, 5이고 다음 자릿수가 5 이상인 경우
        if digit > 5 or (digit == 5 and next_digit >= 5):
            answer += (10 - digit)  # 위로 올림 (10에서 현재 자릿수를 뺀 값을 더함)
            storey += 10  # 다음 자릿수에 1을 올림
        else:
            answer += digit  # 아래로 내림 (현재 자릿수 값을 그대로 더함)
        
        storey //= 10  # 처리 완료한 자릿수 제거
    
    return answer  # 최종적으로 필요한 마법의 돌 개수 반환