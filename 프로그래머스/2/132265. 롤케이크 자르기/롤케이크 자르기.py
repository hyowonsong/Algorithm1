def solution(topping):
    answer = 0
    cheolsu = {}
    brother = {}

    # 철수 세팅
    for i in topping:
        if i not in cheolsu:
            cheolsu[i] = 1
        else:
            cheolsu[i] += 1

    # 동생한테 하나씩 주면서 cheolsu는 하나씩 빼기
    for i in topping:
        cheolsu[i] -= 1
        if cheolsu[i] == 0:
            del cheolsu[i]
        
        if i not in brother:
            brother[i] = 1
        else:
            brother[i] += 1
        
        if len(cheolsu) == len(brother):
            answer += 1

    return answer
