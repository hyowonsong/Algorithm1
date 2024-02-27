def solution(n):
    answer = 0
    sum = 0
    
    for i in range(1,n+1):
        sum = 0
        for j in range(i, n+1):    # j는 i부터 더해나가는 역할
            sum += j
            
            if sum == n:           # 합계가 n과 같다면 answer +=1 
                answer +=1
                break
                
            elif sum > n:
                break
            
    return answer 