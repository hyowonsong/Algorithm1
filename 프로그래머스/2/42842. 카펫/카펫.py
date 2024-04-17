def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for w in range(1, total + 1):
        if total % w == 0:
            h = total // w
            if (w - 2) * (h - 2) == yellow:
                answer.append(h)
                answer.append(w)
                break
                
    return answer
