def solution(k,tangerine):
    answer = 0
    a = {}
    
    for i in tangerine:
        if i in a:
            a[i] += 1         # 딕셔너리 value 값 올려주기
        else:
            a[i] = 1
    
    a = dict(sorted(a.items(), key = lambda x: x[1], reverse = True))
    for i in a:
        if k<=0 : 
            return answer
        k -= a[i]                      #딕셔너리의 value 값 만큼 빼준다.
        answer +=1
    return answer