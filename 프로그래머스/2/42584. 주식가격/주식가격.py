def solution(prices):
    answer = [0] * len(prices) # 결과를 저장할 배열 초기화
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            # 현재 가격보다 떨어지는 경우가 나타날 때까지 시간을 증가시킴
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
            # 가격이 떨어지지 않은 경우
            elif j == len(prices) - 1:
                answer[i] = j - i
                
    return answer
