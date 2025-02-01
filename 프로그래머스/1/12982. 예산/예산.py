def solution(d, budget):
    d.sort()
    answer = 0

    for i in d:
        if i <= budget:
            budget -= i
            answer += 1
        else:
            return answer
        
    return answer