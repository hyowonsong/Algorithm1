def solution(a, b, n):
    answer = 0
    
    while (n>=a):
        bottle = n%a
        
        n = (n//a)*b       # 마트에서 받는 콜라의 수  
        answer +=n         # 빈병 개수 만큼 answer 에서 +
        n+= bottle         # 남아 있는 병을 더해줘야 다시 while 문 돌때 포함된다.
        
    return answer