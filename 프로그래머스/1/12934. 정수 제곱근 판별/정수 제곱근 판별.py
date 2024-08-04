import math 

def solution(n):
    new = math.sqrt(n)
    
    # is_integer() 를 생각해야 한다!
    if new.is_integer():
        return int((new+1)**2)
    else:
        return -1