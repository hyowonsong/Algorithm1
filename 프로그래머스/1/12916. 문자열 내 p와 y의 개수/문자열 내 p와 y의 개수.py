# 문자열 내 p와 y의 개수
def solution(s):
    answer1 = 0
    answer2 = 0
    
    s = s.lower()
    for i in s:
        if i == 'p':
            answer1 +=1
        elif i == 'y':
            answer2 +=1
        
    if answer1 == answer2:
        return True
    else:
        return False