# 예산

def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget<i:
            return answer
        else:
            budget = budget - i
            answer+=1
    return answer