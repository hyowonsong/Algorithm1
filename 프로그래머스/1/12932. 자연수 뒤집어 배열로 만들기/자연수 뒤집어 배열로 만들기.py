def solution(n):
    answer = []
    new = str(n)
    
    for i in new:
        answer.append(int(i))

    
    return answer[::-1]