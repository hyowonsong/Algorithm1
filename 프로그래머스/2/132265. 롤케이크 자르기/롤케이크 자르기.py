def solution(topping):
    answer = 0
    cheoulsu = {}
    brother = {}

    # 처음엔 cheoulsu가 모든 토핑을 가지고 있다.
    for i in topping:
        if i in cheoulsu:
            cheoulsu[i] += 1
        else:
            cheoulsu[i] = 1

    # 형이 하나씩 토핑을 가져감
    for i in topping:
        cheoulsu[i] -= 1
        if cheoulsu[i] == 0:
            del cheoulsu[i]

        if i in brother:
            brother[i] += 1
        else:
            brother[i] = 1

        # 현재 cheoulsu와 brother의 종류 개수를 비교
        if len(cheoulsu) == len(brother):
            answer += 1

    return answer
