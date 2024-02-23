# 히샤드 수

def solution(x):

    new = sum(map(int,str(x)))
    
    if x % new == 0:
        return True
    else:
        return False
