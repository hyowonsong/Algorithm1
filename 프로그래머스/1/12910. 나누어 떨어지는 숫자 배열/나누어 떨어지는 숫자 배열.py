# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    
    for i in arr:
        # i를 다시 divisor 로 나누어야
        if i% divisor ==0:
            answer.append(i)
            
    if len(answer) == 0:
        answer = [-1]
    else:
        answer.sort()
            
    return answer