import math

def solution(n):
    answer = 0
    new = math.sqrt(n)
    
    if new.is_integer():
        answer = ((new+1)**2)
        
    else:
        answer = -1
        
    return answer